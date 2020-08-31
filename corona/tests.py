from django.test import TestCase
from .models import *

# Create your tests here.
class TestTreatment(TestCase):
    def setUp(self):
        self.assigned_treatment = Treatment(treatment = "Positive")

    def test_instance(self):
        self.assertTrue(isinstance(self.assigned_treatment,Treatment))

class TestStatus(TestCase):
    def setUp(self):
        self.active = Status(status = "home care")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.active,Status))

class TestDoctor(TestCase):
    def setUp(self):
        self.names = Doctor(name = "Doc")
        self.clinic = Doctor(hospital = "Mayo Clinic")
        self.tel = Doctor(phone = "0700123456")
        self.username = User(id=1, username="mack")
        self.username.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.names,Doctor))
        self.assertTrue(isinstance(self.clinic,Doctor))
        self.assertTrue(isinstance(self.tel,Doctor))
        self.assertTrue(isinstance(self.username, User))

    def test_save_user(self):
        self.username.save()

    def test_delete_user(self):
        self.username.delete

class TestPatient(TestCase):
    def setUp(self):
        self.mack = Patient(name = "Patient 0")
        self.tel = Patient(phone = "0700123456")
        self.town = Patient(location = "Machakos")
        self.username = User(id=1, username="moringa")
        self.username.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mack,Patient))
        self.assertTrue(isinstance(self.tel,Patient))
        self.assertTrue(isinstance(self.town,Patient))
        self.assertTrue(isinstance(self.username, User))

    def test_save_user(self):
        self.username.save()

    def test_delete_user(self):
        self.username.delete

class TestReport(TestCase):
    def setUp(self):
        self.username = User.objects.create(id=1, username="moringa")
        self.celcius = Report(temp = "32")
        self.tech = Report(kit = "1234")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.celcius,Report))
        self.assertTrue(isinstance(self.tech,Report))

if __name__ == '__main__':
    unittest.main() 