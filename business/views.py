# External Import
import business
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic.edit import FormMixin

# Internal Import
from worker.models import Worker
from bookmark.models import Bookmark
from business.models import Business
from review.models import Review

from worker.models import *
from .forms import ReviewForm


class BusinessListPageView(UserPassesTestMixin, ListView):
    template_name = "business/business-list-page.html"
    paginate_by = 10

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_customer
        return True

    # Redirect user to who doesn't have permission to access this page
    def handle_no_permission(self):
        if self.request.user.is_business:
            return redirect('businessDash')
        elif self.request.user.is_staff:
            return redirect('my-admin-dashboard')
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_bookmarks_business = []
        if self.request.user.is_authenticated and self.request.user.is_customer:
            customer_bookmarks = Bookmark.objects.filter(
                customer=self.request.user.customer).values_list('business', flat=True)
            customer_bookmarks_business = [Business.objects.get(id=id) for id in
                                           customer_bookmarks]
        query = self.request.GET.get('q')
        if query is not None:
            context["query"] = query

        context["customer_bookmarks_business"] = customer_bookmarks_business
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None and query != '':
            return Business.objects.search(query).active().distinct()
        return Business.objects.all()


class BusinessProfileView(UserPassesTestMixin, FormMixin, DetailView):
    queryset = Business.objects.all()
    template_name = "business/business-profile.html"
    slug_url_kwarg = 'slug'
    form_class = ReviewForm

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_customer
        return True

    # Redirect user to who doesn't have permission to access this page
    def handle_no_permission(self):
        if self.request.user.is_business:
            return redirect('businessDash')
        elif self.request.user.is_staff:
            return redirect('my-admin-dashboard')
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        worker = Worker.objects.filter(business__slug=slug)
        context["Worker"] = worker
        review = Review.objects.filter(business__slug=slug)
        context["review"] = review
        current_user_business_review = Review.objects.get(
            customer=self.request.user.customer, business=self.object)
        context["form"] = ReviewForm(instance=current_user_business_review)
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        user_business_review = Review.objects.get(
            customer=request.user.customer, business=self.object)
        if form.is_valid():
            if not user_business_review:
                review = form.save(commit=False)
                review.business = self.object
                review.customer = self.request.user.customer
                review.save()
            else:
                user_business_review.comment = form.cleaned_data.get('comment')
                user_business_review.rating = form.cleaned_data.get('rating')
                user_business_review.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('business-profile', kwargs={'slug': self.object.slug})
