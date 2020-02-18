from django.db import models
from django.urls import reverse

# Create your models here.
class IceCream(models.Model):
    flavor = models.CharField(max_length=50)

    base_choices = [
        ('chocolate'), ('vanilla')
    ]
    base = models.CharField(max_length=20, choices=base_choices, default='vanilla') 

    available_choices= [
        ('daily'), ('weekly'), ('seasonal')
    ]
    available = models.CharField(max_length=20, choices=available_choices, default='daily')

    featured = models.BooleanField()

    date_churned = models.DateField()

    def __str__(self):
        return self.flavor
        return self.base_choices
        return self.available_choices

        def get_absolute_url(self):
            return reverse('icecream:index')