from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    """Subtract the arg from the value."""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return value


@register.filter
def times(number):
    """Return a range of numbers for iteration."""
    try:
        return range(int(number))
    except (ValueError, TypeError):
        return range(0)
