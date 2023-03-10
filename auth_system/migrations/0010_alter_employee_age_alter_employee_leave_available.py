# Generated by Django 4.1.5 on 2023-03-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_system", "0009_alter_employee_leave_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="age",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="employee",
            name="leave_available",
            field=models.CharField(default="30", editable=False, max_length=10),
        ),
    ]