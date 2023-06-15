from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #teacher = models.ForeignKey("Staff", on_delete=models.CASCADE)
    age = models.IntegerField()
    grade_level = models.IntegerField()
    balance = models.IntegerField()