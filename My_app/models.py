from django.db import models
from django.urls import reverse

class PredResult(models.Model):
    wind_speed= models.DecimalField(max_digits=10,decimal_places=5)
    wind_direction= models.DecimalField(max_digits=10,decimal_places=5)
    atmospheric_temperature= models.DecimalField(max_digits=10,decimal_places=5)
    atmospheric_pressure= models.DecimalField(max_digits=10,decimal_places=5)
    prediction = models.FloatField()

    def get_absolute_url(self):
        return reverse('My_app-predict')