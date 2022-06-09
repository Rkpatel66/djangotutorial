from django.db import models

# Create your models here.


class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=250)
