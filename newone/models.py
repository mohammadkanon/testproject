from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField


class PhoneModel(models.Model):
    name = models.CharField(max_length=128)
    phone = PhoneField(max_length=20, unique=True)


