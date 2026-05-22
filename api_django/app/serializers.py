from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'status']


class BookActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['status']
        read_only_fields = ['id', 'title', 'author']
