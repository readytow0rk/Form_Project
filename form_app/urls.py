# form_app/urls.py
from django.urls import path
from .views import submit_form

urlpatterns = [
    path('', submit_form, name='submit_form'),
]