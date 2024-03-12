# Generated by Django 5.0.2 on 2024-03-11 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("document_app", "0001_initial"),
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourtLevel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Case",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("judge_or_arbitrator", models.CharField(max_length=100)),
                ("scheduling_date", models.DateTimeField()),
                ("documents", models.ManyToManyField(to="document_app.document")),
                (
                    "lawyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.userprofile",
                    ),
                ),
                (
                    "court_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="case_app.courtlevel",
                    ),
                ),
            ],
        ),
    ]
