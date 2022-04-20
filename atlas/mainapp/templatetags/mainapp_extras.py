from django import template
from mainapp.models import DataModel

register = template.Library()


@register.filter
def in_employees(user):
    return DataModel.objects.get(sts=user)