# Generated by Django 4.2.5 on 2023-09-07 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0004_alter_uservotes_answer"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="uservotes", unique_together={("question", "username", "answer")},
        ),
    ]
