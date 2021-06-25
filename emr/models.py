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

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'


class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    dob = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    notes = models.TextField()

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'

class Vitals(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    temperature = models.FloatField()
    pulse = models.IntegerField()
