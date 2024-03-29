# Generated by Django 5.0.2 on 2024-03-18 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case_app", "0002_court_courttype"),
        ("user_app", "0002_remove_userprofile_user_customuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="lawyer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user_app.customuser"
            ),
        ),
        migrations.AddField(
            model_name="case",
            name="court",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="case_app.court",
            ),
        ),
        migrations.AddField(
            model_name="court",
            name="court_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="case_app.courttype"
            ),
        ),
    ]
