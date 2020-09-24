"""
Created on 03-Aug-2020

@author: shankar
"""
from ..models import Team
from django import template
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import stringfilter
from cricket.settings import MATCH_CHOICE

register = template.Library()


@register.filter
@stringfilter
def get_teamname(value):
    """Removes all values of arg from the given string"""
    try:
        obj = get_object_or_404(Team, pk=value)
        return obj.name
    except Exception:
        for each in MATCH_CHOICE:
            if int(value) == each[0]:
                return each[1]
        return "Not Played"
