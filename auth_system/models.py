from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
# Create your models here.
class Employee(models.Model):
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    age =models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    company_name = models.CharField(max_length=60)
    department_name = models.CharField(max_length=100)
    leave_available = models.PositiveIntegerField(default=30,editable=True)

class holiday(models.Model):
    date = models.DateField("Date (yyyy-mm-dd)",auto_now_add=False, auto_now=False, blank=True,null=True)
    name = models.CharField(max_length=50)

class employee_leave(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Start_date = models.DateField("Start Date (yyyy-mm-dd)",auto_now_add=False,auto_now=False,blank=True,null=True)
    End_date = models.DateField("End Date (yyyy-mm-dd)",auto_now_add=False, auto_now=False, blank=True,null=True)
    reason = models.CharField(max_length=500)

