from django.db import models
from django.urls import reverse


# Create your models here.
class Business(models.Model):
    first = models.CharField(max_length=15)
    last = models.CharField(max_length=15)
    Designation = models.CharField(max_length=20)
    Company = models.CharField(max_length=15)
    contact = models.BigIntegerField()
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('business_card')

    def __str__(self):
        return self.email
