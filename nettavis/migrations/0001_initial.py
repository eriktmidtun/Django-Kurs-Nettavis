# Generated by Django 3.1.6 on 2021-02-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikkel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittel', models.CharField(max_length=200, verbose_name='Tittel')),
                ('skrevet_av', models.CharField(max_length=300, verbose_name='Skrevet av')),
                ('bilde', models.ImageField(upload_to='opplastninger/bilder', verbose_name='Bilde')),
                ('bilde_kredittering', models.CharField(default='Foto: ', help_text='Vennligst oppgi kredittering for bilde.', max_length=200, verbose_name='Bildekredittering')),
                ('publisert', models.DateTimeField(auto_now_add=True)),
                ('sist_oppdatert', models.DateTimeField(auto_now=True)),
                ('ingress', models.CharField(max_length=200, verbose_name='Ingress')),
                ('brodtekst', models.TextField(verbose_name='Brødtekst')),
            ],
            options={
                'verbose_name': 'Artikkel',
                'verbose_name_plural': 'Artikler',
            },
        ),
    ]
