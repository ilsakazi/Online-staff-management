from django import forms
from .models import *

class facform(forms.ModelForm):
    class Meta:
        model=Faculty
        fields='__all__'
        #fields=['name','Email']