from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def validate_capitalized(value):
    if value[0] != value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!',
                              code='invalid',
                              params={'value': value})


class UserModel(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=20, validators=[validate_capitalized])
    last_name = models.CharField(max_length=20, validators=[validate_capitalized])
    profile_picture = models.URLField(max_length=200)


