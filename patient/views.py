from rest_framework import generics
from .serializers import PatientSerializer
from .models import Patient

# class PatientList(generics.ListAPIView):
#   queryset = Patient.objects.all()
#   serializer_class = PatientSerializer

class PatientList(generics.ListCreateAPIView):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer

# class PatientDetail(generics.RetrieveAPIView):
#   queryset = Patient.objects.all()
#   serializer_class = PatientSerializer

# class PatientDetail(generics.RetrieveUpdateAPIView):
#   queryset = Patient.objects.all()
#   serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer

