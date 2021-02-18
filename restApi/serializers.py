from nettavis.models import Artikkel
from rest_framework import serializers

class ArtikkelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikkel
        fields = ("id", "tittel", "skrevet_av", "bilde", "bilde_kredittering",
                   "ingress", "brodtekst","publisert", "sist_oppdatert")
    publisert = serializers.CharField(source='formater_publisert')
    sist_oppdatert = serializers.CharField(source='formater_sist_oppdatert')