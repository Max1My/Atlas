from django import template

register = template.Library()


@register.filter
def in_employees(employees, users):
    return employees.filter(users=users)