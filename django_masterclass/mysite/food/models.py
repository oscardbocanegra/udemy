from django.db import models

# Create your models here.
class Item(models.Model):
    item_nmae = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()