from django import forms
from django.db import models
from .models import *

class TeacherForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    degree = forms.IntegerField()

class FanForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class YonalishForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = '__all__'