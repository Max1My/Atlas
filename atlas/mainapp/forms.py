from django import forms
from .models import DataModel


class TableForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = ['category_name','current']
        widgets = {
            'category_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'current': forms.TextInput(attrs={ 'class': 'form-control' }),
      }
