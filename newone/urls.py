from django.urls import path
from newone.views import phonenumber

urlpatterns = [
    # ...
    path('', phonenumber, name='phonenumber'),
]