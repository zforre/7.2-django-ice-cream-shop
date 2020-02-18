from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class IceCream(models.Model):
    flavor = models.CharField(max_length=50)

    
    chocolate = 'choc'
    vanilla = 'van'
    base_choices = [
        (chocolate, 'chocolate'), 
        (vanilla, 'vanilla'),
    ]

    base = models.CharField(max_length=20, choices=base_choices, default='vanilla') 

    daily = 'da'
    weekly = 'we'
    seasonal = 'se'
    available_choices= [
        (daily,'daily'), 
        (weekly,'weekly'), 
        (seasonal,'seasonal')
    ]

    available = models.CharField(max_length=20, choices=available_choices, default='daily')

    # featured = models.BooleanField()

    date_churned = models.DateField(default=date.today)

    def __str__(self):
        return self.flavor
        

        def get_absolute_url(self):
            return reverse('icecream:index')




            