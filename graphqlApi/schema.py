import graphene
from graphene_django import DjangoObjectType

from .utils import get_offset

from nettavis.models import Artikkel


class ArtikkelType(DjangoObjectType):
    class Meta:
        model = Artikkel
        fields = ("id", "tittel", "skrevet_av", "bilde", "bilde_kredittering",
                   "ingress", "brodtekst")

    sist_oppdatert = graphene.String()
    publisert = graphene.String()

    def resolve_publisert(artikkel, info):
        return artikkel.formater_publisert()
    
    def resolve_sist_oppdatert(artikkel, info):
        return artikkel.formater_sist_oppdatert()

class Query(graphene.ObjectType):
    alle_artikler = graphene.List(ArtikkelType, offset=graphene.Int(), count=graphene.Int())
    artikkel = graphene.Field(ArtikkelType, id=graphene.Int())

    def resolve_alle_artikler(root, info, offset=None ,count=None):
        artikler = Artikkel.objects.all()
        if count and not offset:
            return get_offset(artikler,0,count)
        return get_offset(artikler,offset,count)
    
    def resolve_artikkel(root, info, id):
        return Artikkel.objects.get(pk=id)

schema = graphene.Schema(query=Query)