# form_app/views.py
from django.shortcuts import render, redirect
from .forms import PaymentForm

def privacy_policy(request):
    return render(request, 'form_app/privacyPolicy.html')  

def home(request):
    return render(request, 'form_app/index.html')  

def submit_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  
    else:
        form = PaymentForm()

    return render(request, 'success.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

