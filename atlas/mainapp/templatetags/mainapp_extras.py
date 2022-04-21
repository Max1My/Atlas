from django import template
from mainapp.models import DataModel

register = template.Library()


@register.simple_tag()
def get_employee(user):
    return DataModel.objects.filter(sts=user)

