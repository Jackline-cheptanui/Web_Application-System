from audioop import reverse
import datetime
from django.test import TestCase

# Create your tests here.
def test_full_name_contains_first_name(self):
        self.assertIn(self.patient.first_name,self.patient.full_name())
    
def test_full_name_contains_last_name(self):
        self.assertIn(self.patient.last_name,self.patient.full_name())
    
def test_patient_number(self):
        self.assert_(self.patient.patient_number())
        
def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.patient.age
        self.assertEqual(year,self.patient.year_of_birth())
def test_general_health(self):
            self.assert_(self.patient.general_health())
    
def test_patient_registration_view(self):
        url=reverse('patient:register_patient')
        data ={"first_name":self.patient.first_name,
               "last_name":self.patient.last_name,
               "registration_date":self.patient.registration_date,
                "date_of_birth":self.patient.date_of_birth,
               "gender":self.patient.gender,
        }
        request=self.client.post(url,data,follow=True)
        self.assertEqual(request.status_code,200)