import datetime

from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from books.models import BookEntity
from books.serializers import BookSerializers

title__icontains = openapi.Parameter('title__icontains', openapi.IN_QUERY,
                                     description="return the books with this title", type=openapi.TYPE_STRING)
category__icontains = openapi.Parameter('category__icontains', openapi.IN_QUERY,
                                        description="return books in this category", type=openapi.TYPE_STRING)
created_at = openapi.Parameter('created_at', openapi.IN_QUERY, description="return all books created in this time",
                               type=openapi.TYPE_STRING)


@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[title__icontains, category__icontains, created_at]))
class BookViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet,
                  mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = BookEntity.objects.all()
    serializer_class = BookSerializers
    filters_fields = ['title__icontains', 'category__icontains', 'created_at']

    def get_queryset(self):
        query_params = self.request.query_params
        queryset = self.queryset
        filters = {}
        for field in self.filters_fields:
            if field in query_params and query_params[field] != 'null':
                if field == 'created_at':
                    date = datetime.datetime.strptime(query_params[field], '%Y/%m/%d').date()
                    filters['created_at__date'] = date
                else:
                    filters[field] = query_params[field]
        queryset = queryset.filter(**filters)
        return queryset


class ReadBookViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BookEntity.objects.all()
    serializer_class = BookSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data['body']
        return Response(data)
