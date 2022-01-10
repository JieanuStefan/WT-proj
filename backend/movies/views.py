from django.http import HttpResponse
from .models import Movie
from rest_framework import viewsets, permissions, generics
from .serializers import MoveSerializer
from rest_framework import filters
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoveSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

@csrf_exempt
def email_conf(request):
    if request.method=="POST":
        data = json.loads(request.body)
        print(data['email'])

        send_mail(
            'Movie Rent Order Confirmation',
            'This message was sent to confirm your movie rental',
            'rentamovieproject@gmail.com',
            [data['email']],
            fail_silently=False,
        )
    return HttpResponse('ok')

