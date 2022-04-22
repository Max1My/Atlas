from django.urls import reverse_lazy
from django.views.generic import CreateView
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.views.generic import View
from django.http import JsonResponse

from .models import DataModel
from .forms import TableForm


class TableCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = DataModel
    template_name = 'mainapp/add.html'
    form_class = TableForm
    title = 'Добавление'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.sts = self.request.user
        return super(TableCreateView, self).form_valid(form)


@login_required(login_url='/auth/login/')
def index(request):
    if request.method == 'GET' and 'current' in request.GET:
        value = request.GET['current']
        sts_id = request.GET['sts_id']
        print(value)
        print(sts_id)
        if value is not None and value != '':
            value = float(request.GET.get('current'))
            value += 0
            DataModel.objects.create(
                current=value,
                sts_id=sts_id
            )
            return JsonResponse({'data': value}, status=200)

    if request.user.id == 1:
        users = User.objects.all()
        employees = DataModel.objects.all()
        content = {
            'users': users,
            'employees': employees
        }
    else:
        employees = DataModel.objects.filter(sts_id=request.user.id)
        content = {
            'employees': employees,
        }
    return render(request, "mainapp/index.html", content)

    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            data = form.save()
            return JsonResponse({"msg": "Data successfully saved.", "data": data.value})
        else:
            return JsonResponse({"msg": "Invalid data", "data": None})
    else:
        form = TableForm()
        return render(request, 'mainapp/index.html', {"form": form})


@login_required(login_url='/auth/login/')
def update(request, id):
    employee = DataModel.objects.get(id=id)
    form = TableForm(request.POST, instance=employee)
    if form.is_valid():
        try:
            form.save()
            return redirect("/")
        except Exception as e:
            pass
    return render(request, 'mainapp/edit.html', {'employee': employee})


@login_required(login_url='/auth/login/')
def destroy(request, id):
    employee = DataModel.objects.get(id=id)
    employee.delete()
    return redirect("/")
