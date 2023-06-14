from django.db import models

class ItemType(models.Model):
    item_type = models.CharField(max_length=255)