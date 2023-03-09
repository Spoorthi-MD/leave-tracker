from django.forms import ModelForm
from auth_system.models import Employee,employee_leave
class Employee_form(ModelForm):
    class Meta:
        model = Employee

        fields = '__all__'

class leave_form(ModelForm):
    class Meta:
        model = employee_leave

        fields = '__all__'


