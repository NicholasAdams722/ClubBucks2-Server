from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)