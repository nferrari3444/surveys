from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=100)
    # password = forms.CharField(widget = forms.PasswordInput)
    password = models.CharField(_('password'), max_length=128, default='')
    email =  models.EmailField(max_length=254, blank=False, unique=True, default='',
                               

        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)


class Survey(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    topic = models.CharField(max_length=50, default='hola')
    question = models.CharField(max_length=200)
    creator = models.CharField(max_length=100)
    submissions = models.IntegerField(default=0)

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
   # user = models.CharField(max_length=50)
