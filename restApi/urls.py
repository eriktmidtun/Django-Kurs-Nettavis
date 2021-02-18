from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('artikler/',views.ArtikkelList.as_view()),
    path('artikler/<int:pk>/',views.ArtikkelDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


