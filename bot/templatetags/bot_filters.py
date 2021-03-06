from django import template

register = template.Library()

@register.filter
def current_hp(value):
    return int(float(value.split('|')[0]))
    
@register.filter
def max_hp(value):
    return int(value.split('|')[1])

@register.filter
def line_hp(value, line_length):
    current_hp = float(value.split('|')[0])
    max_hp = float(value.split('|')[1])
    return int(round(float(line_length) * current_hp / max_hp))