# form_app/urls.py
from django.urls import path
from .views import submit_payment, privacy_policy, home, success_page, checkout

urlpatterns = [
    path('', home, name='home'),
    path('checkout',checkout, name='checkout'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('submit_payment/', submit_payment, name='submit_payment'),
    path('success/', success_page, name='success_page'),
]





