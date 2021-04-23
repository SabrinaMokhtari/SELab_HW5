from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from books.models import BookEntity


class BookSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.pop('pipeline_id', None)
        return super().create(validated_data)

    def to_representation(self, instance):
        """method for customizing object representation"""
        representation = super(BookSerializers, self).to_representation(instance)
        return representation

    class Meta:
        model = BookEntity
        fields = ['id', 'title', 'category', 'status', 'body', 'created_at']


class ReadBookSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.pop('pipeline_id', None)
        return super().create(validated_data)

    def to_representation(self, instance):
        """method for customizing object representation"""
        representation = super(BookSerializers, self).to_representation(instance)
        return representation

    class Meta:
        model = BookEntity
        fields = ['id', 'body']
