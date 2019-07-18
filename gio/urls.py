from django.urls import path
from gio.views import position

urlpatterns = [
    # ...
    path('', position, name='position'),
]