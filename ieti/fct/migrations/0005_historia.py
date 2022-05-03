# Generated by Django 3.2 on 2022-04-28 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fct', '0004_auto_20220428_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('pasoInicial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasoInicial', to='fct.paso')),
            ],
        ),
    ]