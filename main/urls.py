
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', BloggerDocumentViewSet.as_view({'get':'list'}))
]