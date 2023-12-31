from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.ForeignKey('ItemType', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    quantity = models.IntegerField() 