from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Doctor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')


class Vitals(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    pulse = models.IntegerField()


class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    dob = models.DateField()
    vitals = models.ForeignKey(Vitals, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    notes = models.TextField()
