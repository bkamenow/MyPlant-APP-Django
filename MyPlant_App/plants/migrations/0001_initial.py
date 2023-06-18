# Generated by Django 4.2.2 on 2023-06-18 20:23

import MyPlant_App.plants.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ODP', 'Outdoor Plants'), ('IDP', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), MyPlant_App.plants.models.only_letters_validator])),
                ('image', models.URLField()),
                ('description', models.TextField(max_length=255)),
                ('price', models.FloatField(max_length=8)),
            ],
        ),
    ]
