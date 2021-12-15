from django.http import HttpResponse
from .models import Movie
from rest_framework import viewsets, permissions, generics
from .serializers import MoveSerializer
from rest_framework import filters

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoveSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

