from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class IceCream(models.Model):
    flavor = models.CharField(max_length=50)

    CHOCOLATE = 'choc'
    VANILLA = 'van'
    base_choices = [
        (CHOCOLATE, 'CHOCOLATE'), 
        (VANILLA, 'VANILLA'),
    ]

    base = models.CharField(max_length=20, choices=base_choices, default='vanilla') 

    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    SEASONAL = 'SEASONAL'
    available_choices= [
        (DAILY,'daily'), 
        (WEEKLY,'weekly'), 
        (SEASONAL,'seasonal')
    ]

    available = models.CharField(max_length=20, choices=available_choices, default='daily')

    featured = models.BooleanField(default=False)

    date_churned = models.DateField(default=date.today)

    class Meta:
        ordering = ['flavor']

    def __str__(self):
        return self.flavor
        

    def get_absolute_url(self):
            return reverse('ice_cream:index')




            