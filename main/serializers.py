from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django_elasticsearch_dsl_drf import DocumentSerializer
from .documents import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author = Userserializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Blog 
        document = BlogDocument
        fields = "__all__"
        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
