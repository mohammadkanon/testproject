from django.urls import path
from dmqurey.views import makequrey

urlpatterns = [
    path('', makequrey, name='makequrey'),
]