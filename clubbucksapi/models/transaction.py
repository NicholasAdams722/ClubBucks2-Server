from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    created_on = models.DateTimeField()
    completed_on = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField("Item", through="TransactionItem")