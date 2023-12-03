from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import submit_payment, success_page, checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_app.urls')),
    path('submit_payment/', submit_payment, name='submit_payment'),
    path('success/', success_page, name='success_page'),
    path('checkout/', checkout, name='checkout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urls.py



