# Generated by Django 4.2.5 on 2023-09-07 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0007_alter_uservotes_question_name"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="uservotes", unique_together={("username", "answer")},
        ),
    ]