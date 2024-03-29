# Generated by Django 5.0.2 on 2024-03-18 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("authentication_manager", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="auth_user_groups",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("partner", "Partner"),
                    ("associate", "Associate"),
                    ("clerk", "Clerk"),
                    ("secretary", "Secretary"),
                    ("admin", "Admin"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                related_name="auth_user_permissions",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
