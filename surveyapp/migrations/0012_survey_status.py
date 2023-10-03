# Generated by Django 4.2.5 on 2023-09-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0011_alter_uservotes_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Running", "Running"),
                    ("Finished", "Finished"),
                ],
                default="Running",
                max_length=15,
            ),
            preserve_default=False,
        ),
    ]