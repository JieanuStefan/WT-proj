from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Movie

class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
