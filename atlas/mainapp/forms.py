from django import forms
from .models import DataModel


class TableForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = ['current']
        widgets = {
            'current': forms.TextInput(attrs={ 'class': 'form-control' }),
      }
