# Generated by Django 4.2.5 on 2023-09-07 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0008_alter_uservotes_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="uservotes", unique_together=set(),),
    ]
