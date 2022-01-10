from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.MovieViewSet)

urlpatterns = [
    path('confirmation', views.email_conf),
    path('', include(router.urls)),
]