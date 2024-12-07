from django import forms
from .models import InputTable

class InputTableForm(forms.ModelForm):
    class Meta:
        model = InputTable
        fields = ['input1', 'input2', 'input3']
