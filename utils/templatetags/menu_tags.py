from django import template
from django.conf import settings
from django.core.cache import cache

from basic.models import BasicPage

register = template.Library()

@register.simple_tag()
def get_nav_items():
    return BasicPage.objects.live().public().in_menu()
