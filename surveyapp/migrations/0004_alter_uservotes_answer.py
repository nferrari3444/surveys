# Generated by Django 4.2.5 on 2023-09-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0003_alter_uservotes_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservotes",
            name="answer",
            field=models.CharField(max_length=50),
        ),
    ]
