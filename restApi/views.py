from nettavis.models import Artikkel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArtikkelSerializer

from django.shortcuts import get_object_or_404

class ArtikkelList(APIView):
    def get(self, request, format=None):
        artikler = Artikkel.objects.all()
        serializer = ArtikkelSerializer(artikler, many=True)
        return Response(serializer.data)

class ArtikkelDetail(APIView):
    def get(self,request, pk , format=None):
        artikkel = get_object_or_404(Artikkel, id=pk)
        serializer = ArtikkelSerializer(artikkel)
        return Response(serializer.data)
