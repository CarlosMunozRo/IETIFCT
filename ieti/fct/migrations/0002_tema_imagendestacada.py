# Generated by Django 3.2 on 2022-05-14 16:17

from django.db import migrations, models
import fct.models


class Migration(migrations.Migration):

    dependencies = [
        ('fct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='imagenDestacada',
            field=models.ImageField(blank=True, null=True, upload_to=fct.models.get_temas_images_path),
        ),
    ]
