from django.db import models

# Create your models here.


class PaymentPlan(models.Model):
    """The plans available for purchase"""
    
    
    sku = models.CharField(unique=True, max_length=255)
    name = models.CharField(unique=True, max_length=255)
    price = models.IntegerField()
