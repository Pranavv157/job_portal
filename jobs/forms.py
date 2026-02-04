from django import forms
from .models import Job
from .models import Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['recruiter']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']
