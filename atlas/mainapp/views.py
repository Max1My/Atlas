from django.contrib.auth.models import User
from django.template.defaultfilters import register
from django.urls import reverse_lazy
from django.views.generic import CreateView
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import DataModel
from .forms import TableForm


class TableCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = DataModel
    template_name = 'mainapp/index.html'
    form_class = TableForm
    title = 'Добавление'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.sts = self.request.user
        return super(TableCreateView, self).form_valid(form)


@login_required(login_url='/auth/login/')
def index(request):
    if request.user.id == 1:
        users = User.objects.all()
        employees = DataModel.objects.all()
        content = {
            'employees':employees,
            'users':users
        }
    else:
        employees = DataModel.objects.filter(sts=request.user.id)
        content = {
            'employees': employees,
        }
    return render(request, "mainapp/chart.html", content)


@login_required(login_url='/auth/login/')
def update(request, id):
    employee = DataModel.objects.get(id=id)
    form = TableForm(request.POST, instance=employee)
    if form.is_valid():
        try:
            form.save()
            print('form save')
            return redirect("/")
        except Exception as e:
            print(e)
    print(form.errors)
    return render(request, 'mainapp/edit.html', {'employee': employee})


@login_required(login_url='/auth/login/')
def destroy(request, id):
    employee = DataModel.objects.get(id=id)
    employee.delete()
    return redirect("/")
