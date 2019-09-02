# Create your models here.
from django.db import models
from django.db.models import CharField, DateTimeField


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created_at: DateTimeField = models.DateTimeField('date created')

    def __str__(self):
        return [self.name, self.description, self.created_at]


class Designs(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title: CharField = models.CharField(max_length=200)
    created_at: DateTimeField = models.DateTimeField('date created')

    def __str__(self):
        return [self.category.name, self.title, self.created_at]
