from django.views.generic import TemplateView,DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import DataModel,Consumption
from .forms import ConsumptionForm

class HomePage(TemplateView):
    template_name = 'mainapp/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = DataModel.objects.all()
        return context

class ConsumptionDetailView(DetailView):
    model = Consumption
    template_name = 'mainapp/table_detail.html'

    def create(request):
        if request.method == 'POST':
            form = ConsumptionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        form = ConsumptionForm()
        return render(request, 'mainapp/table_create.html', {'form': form})

    def edit(request, pk, template_name='mainapp/table_edit.html'):
        table = get_object_or_404(ConsumptionForm, pk=pk)
        form = ConsumptionForm(request.POST or None, instance='post')
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, template_name, {'form': form})

    def delete(request, pk, template_name='mainapp/table_delete.html'):
        contact = get_object_or_404(ConsumptionForm, pk=pk)
        if request.method == 'POST':
            contact.delete()
            return redirect('index')
        return render(request, template_name, {'object': contact})