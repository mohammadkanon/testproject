from django.urls import path
from blog.views import index, add, edit

urlpatterns = [
	path('', index, name='index'),
	path('add/', add, name='add'),
	path('edit/<int:entry_id>/', edit, name='edit'),
]