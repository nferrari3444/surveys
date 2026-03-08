from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Create your models here.
from django.db.models import Count, F, Value

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(_('password'), max_length=128, default='')
    email =  models.EmailField(max_length=254, blank=False, unique=True, default='',
                               
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)


class Survey(models.Model):
    STATUSES = [
        ('Pending', 'Pending'),
        ('Running', 'Running'),
        ('Finished', 'Finished')
    ]

    id = models.AutoField(primary_key=True)
    date = models.DateField()
    topic = models.CharField(max_length=50, default='hola')
    question = models.CharField(max_length=200)
    creator = models.CharField(max_length=100)
    submissions = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUSES, default='Pending')

    def __str__(self):
        return self.question


class Choices(models.Model):
    question = models.ForeignKey(Survey, on_delete=models.CASCADE)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)
    choice_3 =  models.CharField(max_length=100)


class Results(models.Model):
    question = models.ForeignKey(Survey, on_delete=models.CASCADE)
    selectedchoice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
   
  
class Uservotes(models.Model):
    class Meta:
        unique_together = (('username', 'answer'),)

    question_name = models.ForeignKey(Survey, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)
