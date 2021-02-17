from django.urls import path
from . import views

urlpatterns = [
    path('', views.nettavis_template, name='nattavis'),
    path('<int:artikkel_id>/', views.artikkel_template, name="artikkel")
]