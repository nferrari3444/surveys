# Generated by Django 4.2.5 on 2023-09-07 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveyapp", "0006_rename_question_uservotes_question_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservotes",
            name="question_name",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="surveyapp.survey"
            ),
        ),
    ]