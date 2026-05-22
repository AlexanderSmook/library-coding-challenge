from django.shortcuts import render

# Create your views here.

from .models import Book
from rest_framework import views
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookCheckoutView(generics.UpdateAPIView):
#     queryset = Book.objects.filter(status='available')
#     serializer_class = BookUpdateSerializer
#     lookup_field = 'pk'
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.status = 'checked out'
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
