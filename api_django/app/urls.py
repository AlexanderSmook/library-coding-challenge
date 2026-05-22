from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='books-list'), # GET POST
    path('books/<int:pk>/<str:action>/', views.BookActionView.as_view(), name='book-action'), # PUT
    # path('books/search', views.BookSearchView.as_view(), name='book-search'), # GET
]
