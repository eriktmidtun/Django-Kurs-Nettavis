from django.db import models

# Create your models here.

class Artikkel(models.Model):
    class Meta:
        verbose_name = "Artikkel"
        verbose_name_plural = "Artikler"

    tittel = models.CharField('Tittel', max_length=200, blank=False)
    skrevet_av = models.CharField('Skrevet av', max_length=300, blank=False)
    bilde = models.ImageField('Bilde', upload_to='opplastninger/bilder')
    bilde_kredittering = models.CharField('Bildekredittering', blank=False, max_length=200,
                                          default="Foto: ", help_text='Vennligst oppgi kredittering for bilde.')
    publisert = models.DateTimeField(auto_now_add=True, editable=False)
    sist_oppdatert = models.DateTimeField(auto_now=True, editable=False)
    ingress = models.CharField('Ingress', max_length=200)
    brodtekst = models.TextField('Brødtekst')

    def __str__(self):
        return self.tittel
    
    def formater_publisert(self):
        return self.publisert.strftime('%d. %B %Y, %H:%M')

    def formater_sist_oppdatert(self):
        return self.sist_oppdatert.strftime('%d. %B %Y, %H:%M')    