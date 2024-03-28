from django import forms
from admissions.models import student

class studentModelForm(forms.ModelForm):
    class Meta:
        model=student
        fields=("name","fathername")