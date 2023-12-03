# form_app/views.py
from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.http import JsonResponse

def privacy_policy(request):
    return render(request, 'form_app/privacyPolicy.html')  

def home(request):
    return render(request, 'form_app/index.html')  

def submit_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PaymentForm()

    return render(request, 'form_app/payment_form.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

