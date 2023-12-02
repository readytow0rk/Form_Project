# form_app/forms.py
from django import forms
from .models import FormSubmission

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ['email', 'message']
