from django import forms
from .models import *

class leaveform(forms.ModelForm):
    class Meta:
        model = Leaves
        fields  = '__all__'