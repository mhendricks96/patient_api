from django.urls import path
from .views import PatientList, PatientDetail

urlpatterns = [
  path('', PatientList.as_view(), name='patient_list'),
  path('<int:pk>/', PatientDetail.as_view(), name='patient_detail')
]