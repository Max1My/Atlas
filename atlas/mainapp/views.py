from django.views.generic import TemplateView,DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import DataModel
from .forms import DataForm

class HomePage(TemplateView):
    template_name = 'mainapp/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = DataModel.objects.all()
        return context

class DataDetailView(DetailView):
    model = DataModel
    template_name = 'mainapp/table_detail.html'


def create(request,pk):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    current_user = get_object_or_404(User,id=pk)
    form = DataForm()
    content = {
        'user': current_user,
        'form': form
    }
    return render(request, 'mainapp/table_create.html', content)


def edit(request, pk, template_name='mainapp/table_edit.html'):
    table = get_object_or_404(DataForm, pk=pk)
    form = DataForm(request.POST or None, instance='post')
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='mainapp/table_delete.html'):
    contact = get_object_or_404(DataForm, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object': contact})
