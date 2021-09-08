from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Patient

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_patient = Patient.objects.create(
            doctor = testuser1,
            name = 'Jane Doe',
            visit_reason = 'I do not like green eggs and ham, Sam I  am.',
            diagnosis_or_treatment = 'dont eat them',
            birth_date = '1987-12-03'
        )
        test_patient.save()

    def test_patient_content(self):
        patient = Patient.objects.get(id=1)
        actual_doctor = str(patient.doctor)
        actual_name = str(patient.name)
        actual_visit_reason = str(patient.visit_reason)
        self.assertEqual(actual_doctor, 'testuser1')
        self.assertEqual(actual_name, 'Jane Doe')
        self.assertEqual(actual_visit_reason, 'I do not like green eggs and ham, Sam I  am.')