# from attr import fields
from dataclasses import fields
from django.forms import ModelForm
from .models import Student

class Studentform(ModelForm):
    class Meta:
        model =Student
        fields="__all__"
        #exclude=('created_by')