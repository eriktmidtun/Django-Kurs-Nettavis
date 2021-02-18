from django.contrib import admin
from .models import Artikkel
from django_summernote.admin import SummernoteModelAdmin

class ArtikkelAdmin(SummernoteModelAdmin):
    summernote_fields = ('brodtekst',)

admin.site.register(Artikkel, ArtikkelAdmin)