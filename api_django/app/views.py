# from django.shortcuts import render

# Create your views here.

from .models import Book
# from rest_framework import views
from . import serializers
from rest_framework.response import Response
from rest_framework import generics


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

class BookActionView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    allowed_methods = ['PUT']
    serializer_class = serializers.BookActionSerializer
    lookup_field = 'pk'

    def validate_action(self, action, instance):
        if action not in ['checkout', 'return']:
            return "Invalid action: must be 'checkout' or 'return'"
        if action == 'checkout' and instance.status != 'available':
            return "Book is not available"
        if action == 'return' and instance.status != 'checked out':
            return "Book is not checked out"
        return ''

    def update(self, request, *args, **kwargs):
        action = self.kwargs['action']
        instance = self.get_object()
        validation_error = self.validate_action(action, instance)
        if validation_error:
            return Response({'error': f"Invalid action: {validation_error}"}, status=400)
        ## TODO validate that only available books can be checked out and visa versa.

        if action == 'checkout':
            instance.status = 'checked out'
        elif action == 'return':
            instance.status = 'available'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)