from django.urls import path, include
from rest_framework import routers
from books.views import BookViewSet, ReadBookViewSet

router = routers.DefaultRouter()
router.register('list-books', BookViewSet, basename='list-books')
router.register('read-books', ReadBookViewSet, basename='read-books')


urlpatterns = [
    path('', include(router.urls)),
]
