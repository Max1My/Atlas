from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import DataModel
from .forms import TableForm


class HomePage(TemplateView):
    template_name = 'mainapp/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = DataModel.objects.all()
        return context


# class TableCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
#     model = DataModel
#     template_name = 'mainapp/table_create.html'
#     form_class = TableForm
#     title = 'Создание таблицы'
#     success_url = reverse_lazy('mainapp:index')


def addnew(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = TableForm()
    return render(request, 'mainapp/index.html', {'form': form})


def index(request):
    employees = DataModel.objects.all()
    return render(request, "mainapp/chart.html", {'employees': employees})


# def edit(request, id):
#     employee = DataModel.objects.get(id=id)
#     return render(request, 'mainapp/edit.html', {'employee': employee})


def update(request, id):
    employee = DataModel.objects.get(id=id)
    form = TableForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'mainapp/edit.html', {'employee': employee})


def destroy(request, id):
    employee = DataModel.objects.get(id=id)
    employee.delete()
    return redirect("/")
