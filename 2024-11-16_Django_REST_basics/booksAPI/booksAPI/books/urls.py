from django.urls import path

from booksAPI.books import views

urlpatterns = [
    path('', views.ListBooksView.as_view(), name='list-books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
]