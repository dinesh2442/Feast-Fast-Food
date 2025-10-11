from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key))


@register.filter
def multiply(value, arg):
    """Multiply two numbers"""
    try:
        return float(value) * int(arg)
    except (ValueError, TypeError):
        return 0
