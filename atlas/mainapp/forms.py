# from django import forms
# from django.contrib.auth.models import User
# from .models import DataModel
#
# class TableForm(forms.ModelForm):
#     user = forms.ModelChoiceField(queryset=User.objects.all())
#
#     class Meta:
#         model = DataModel
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if field_name == 'sts':
#                 field.widget.attrs['class'] = 'form-control'
#             else:
#                 field.widget.attrs['class'] = 'form-control'


from django import forms
from .models import DataModel


class TableForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = ['sts','category_name','current']
        widgets = {
            'sts': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'category_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'current': forms.TextInput(attrs={ 'class': 'form-control' }),
      }