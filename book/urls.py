from django.urls import path, include
from . import views

app_name = 'Book'
urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('<int:id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('<int:id>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('<int:id>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
]