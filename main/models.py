from django.db import models
from django.contrib.auth.models import User
from .choices import *
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=150, null= False)
    description = models.TextField(null=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    heading = models.CharField(max_length=500, null= False)
    desc = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE, default=0)
    categories = models.ManyToManyField(Category, blank=True)
    created = models.DateTimeField(default= timezone.now)
    def __str__(self):
        return self.heading
    # def type_to_string(self):
    #     if self.type == 'UN':
    #         return 'Unspecified'
    #     elif self.type == 'TU':
    #         return 'Tutorial'
    #     elif self.type == 'RS':
    #         return 'Research'
    #     elif self.type == 'RW':
    #         return 'Review'