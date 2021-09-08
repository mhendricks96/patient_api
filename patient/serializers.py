from rest_framework import serializers
from.models import Patient

class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'birth_date', 'doctor', 'visit_reason', 'diagnosis_or_treatment')
    model = Patient