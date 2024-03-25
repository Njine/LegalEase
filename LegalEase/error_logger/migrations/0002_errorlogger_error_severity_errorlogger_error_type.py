# Generated by Django 5.0.2 on 2024-03-18 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("error_logger", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="errorlogger",
            name="error_severity",
            field=models.CharField(default="medium", max_length=50),
        ),
        migrations.AddField(
            model_name="errorlogger",
            name="error_type",
            field=models.CharField(default="general", max_length=50),
        ),
    ]
