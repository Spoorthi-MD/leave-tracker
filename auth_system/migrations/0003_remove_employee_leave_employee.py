# Generated by Django 4.1.5 on 2023-03-09 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth_system", "0002_remove_employee_user_alter_employee_company_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee_leave",
            name="employee",
        ),
    ]
