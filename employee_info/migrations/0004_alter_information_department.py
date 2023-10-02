# Generated by Django 4.1.3 on 2023-10-02 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("employee_info", "0003_alter_information_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="employee_info.department",
            ),
        ),
    ]
