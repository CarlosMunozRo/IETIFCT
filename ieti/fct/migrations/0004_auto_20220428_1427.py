# Generated by Django 3.2 on 2022-04-28 14:27

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('fct', '0003_auto_20220428_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('nombre', models.CharField(max_length=100)),
                ('texto', tinymce.models.HTMLField()),
                ('tipo', models.CharField(choices=[('PR', 'Pregunta'), ('SO', 'Solucion')], default='PR', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Nodo',
        ),
        migrations.DeleteModel(
            name='NodoPadre',
        ),
    ]
