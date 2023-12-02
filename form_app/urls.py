# form_app/urls.py
from django.urls import path
from .views import submit_form, privacy_policy, home

urlpatterns = [
    path('', home, name='home'),
    path('', submit_form, name='submit_form'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]



