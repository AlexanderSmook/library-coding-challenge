from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='books-list'), # GET POST
    # path('books/<int:pk>/checkout/', views.BookActView.as_view(), name='book-checkout'), # PUT
    # path('books/<int:pk>/return/', views.BookReturnView.as_view(), name='book-return'), # PUT
    # path('books/search', views.BookSearchView.as_view(), name='book-search'), # GET
]
