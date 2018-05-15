from django.db import models
from datetime import date
# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=200)

class Operation(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    a_value = models.DecimalField(max_digits=30, decimal_places=2)
    b_value = models.DecimalField(max_digits=30, decimal_places=2)