from django.urls import path
from post.views import AuthorCreate, AuthorDelete, AuthorUpdate

urlpatterns = [
    # ...
    path('add/', AuthorCreate.as_view(), name='author-add'),
    path('<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]