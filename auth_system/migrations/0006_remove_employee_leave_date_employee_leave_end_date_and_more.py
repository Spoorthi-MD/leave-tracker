# Generated by Django 4.1.5 on 2023-03-10 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_system", "0005_employee_leave_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee_leave",
            name="date",
        ),
        migrations.AddField(
            model_name="employee_leave",
            name="End_date",
            field=models.DateField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 3, 10, 6, 12, 35, 521886, tzinfo=datetime.timezone.utc
                ),
                verbose_name="End Date (dd/mm/yyyy)",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employee_leave",
            name="Start_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Start Date (dd/mm/yyyy)"
            ),
        ),
    ]
