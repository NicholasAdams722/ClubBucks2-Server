from django.db import models

class TransactionItem(models.Model):
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)  #or (blank=True, null=True)