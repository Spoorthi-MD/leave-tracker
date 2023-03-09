from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    age =models.IntegerField()
    gender = models.CharField(max_length=50)
    company_name = models.CharField(max_length=60)
    department_name = models.CharField(max_length=100)
    leave_available = models.IntegerField()

class holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)

class employee_leave(models.Model):
    date = models.DateField()
    reason = models.CharField(max_length=500)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

