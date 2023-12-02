# form_app/views.py
from django.shortcuts import render, redirect
from .forms import FormSubmissionForm

def submit_form(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form_app/success.html')
    else:
        form = FormSubmissionForm()

    return render(request, 'form_app/index.html', {'form': form})
