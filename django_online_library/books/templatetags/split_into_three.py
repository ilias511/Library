from django import template

register = template.Library()


@register.filter
def split_by_three(data):
    return [data[i:i + 3] for i in range(0, len(data), 3)]