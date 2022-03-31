import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import *
from django_elasticsearch_dsl_drf.filter_backends import (FilteringFilterBackend, CompoundSearchFilterBackend)
# Create your views here.


def home(request):
    return HttpResponse({"message":"lollolol"})

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Userserializer
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class BloggerDocumentViewSet(DocumentViewSet):
    document = BlogDocument
    serializer_class = BlogDocumentSerializer
    filter_backend= [CompoundSearchFilterBackend, FilteringFilterBackend]
    search_fields = ('author', 'heading', 'created')
    multi_match_search_fields = ('author', 'heading', 'created')
    fields_fields = {
        'author':'author',
        'heading':'heading',
        'created':'created',
    }