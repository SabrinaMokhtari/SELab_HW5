import datetime

from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from books.models import BookEntity
from books.serializers import BookSerializers


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        data = {'body': serializer.data['body']}
        return Response(serializer.data['body'])


class ReadBookViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BookEntity.objects.all()
    serializer_class = BookSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        data = serializer.data['body']
        return Response(data)
