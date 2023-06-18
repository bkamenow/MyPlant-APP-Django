from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


class PlantModel(models.Model):
    type = models.CharField(max_length=14,
                            choices=[
                                ('ODP', 'Outdoor Plants'),
                                ('IDP', 'Indoor Plants'),
                            ])
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_validator])
    image = models.URLField(max_length=200)
    description = models.TextField(max_length=255)
    price = models.FloatField(max_length=8)

