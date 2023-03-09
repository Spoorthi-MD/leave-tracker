from django.contrib import admin

# Register your models here.
from auth_system.models import Employee,holiday,employee_leave
admin.site.register(Employee)
admin.site.register(holiday)
admin.site.register(employee_leave)