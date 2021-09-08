from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Patient(models.Model):
  name = models.CharField(max_length=64)
  birth_date = models.DateField()
  visit_reason = models.TextField(max_length=600)
  diagnosis_or_treatment = models.TextField(max_length=600)
  doctor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.name

