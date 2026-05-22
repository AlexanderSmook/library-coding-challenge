from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="available", choices=[("available", "Available"), ("checked out", "Checked Out")])

    def __str__(self):
        return f"{self.title} - {self.author}"

