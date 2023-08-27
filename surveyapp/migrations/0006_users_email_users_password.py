# Generated by Django 4.1 on 2023-08-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0005_remove_results_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="email",
            field=models.EmailField(
                default="",
                error_messages={
                    "required": "Please provide your email address.",
                    "unique": "An account with this email exist.",
                },
                max_length=254,
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="password",
            field=models.CharField(default="", max_length=128, verbose_name="password"),
        ),
    ]
