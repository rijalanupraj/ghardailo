from django import template
from notification.models import Notification

register = template.Library()


@register.inclusion_tag('components/navbar_notification.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(
        to_user=request_user).exclude(has_seen=True).order_by('-datetime')
    return {'notifications': notifications}
