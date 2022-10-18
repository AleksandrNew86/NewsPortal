from django import template


register = template.Library()


@register.filter()
def get_subscribes(value):
    subscribers = value.subscribers.all()
    list_subscribers = []
    for i in subscribers:
        list_subscribers.append(i)
    return list_subscribers
