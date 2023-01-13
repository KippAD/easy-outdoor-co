from django import template

register = template.Library()


@register.filter(name='calc_total_price')
def calc_total_price(price, quantity):
    return price * quantity