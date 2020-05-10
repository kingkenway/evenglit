from django import template
from django.template.defaultfilters import stringfilter
from django.template.defaultfilters import linebreaksbr, urlize
import datetime

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

    # {{ somevariable|cut:"0" }}

@register.filter(name='message_color')
def message_color(value):
    """ Returns appropriate color for message tyoe"""
    if value == 'success':
        return 'w3-green'
    else:
        return 'w3-red'


@register.filter(name='event_default_image')
def event_default_image(value):
    """ Returns default image if image url is empty"""
    if not value:
        return "media/event_image/blank101.png"
    else:
        return value


@register.filter(name='lower', is_safe=True)
@stringfilter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

@register.filter(needs_autoescape=True)
def urlize_and_linebreaks(text, autoescape=True):
    return linebreaksbr(
        urlize(text, autoescape=autoescape),
        autoescape=autoescape
    )

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)





# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#assignment-tags
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#default