from business.models import Business
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class BusinessListPageView(UserPassesTestMixin, ListView):
    template_name = "business/business-list-page.html"

    # For Future Use
    def test_func(self):
        # if self.request.user.is_authenticated:
        #     return not self.request.user.is_staff
        return True

    # def handle_no_permission(self):
    #     return redirect('where you want to redirect')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query is not None:
            context["query"] = query
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None and query != '':
            return Business.objects.search(query).active().distinct()
        return Business.objects.all()


class BusinessProfileView(DetailView):
    queryset = Business.objects.all()
    template_name = "business/business-profile.html"
    slug_url_kwarg = 'slug'
