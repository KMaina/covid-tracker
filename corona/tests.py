from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class TestContact(TestCase):
    def setUp(self):
        self.name = Contact(name='George')
        self.email = Contact(email='gkarumbi@gmail.com')
        self.phone = Contact(phone = '0722452772')
        self.location = Contact(location = 'Kigali')
        self.username = User(id=1, username="george")
        self.username.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Contact))
        self.assertTrue(isinstance(self.email,Contact))
        self.assertTrue(isinstance(self.phone,Contact))
        self.assertTrue(isinstance(self.location, Contact))
        self.assertTrue(isinstance(self.username, User))

    def test_save_user(self):
        self.username.save()

    def test_delete_user(self):
        self.username.delete

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('signup')
        self.user = {
            'email' : 'tester@mail.com',
            'username' : 'tester',
            'password' : 'testerpass',
            'password2' : 'testerpass',            
            'fullname' : 'testerfull',
        }

        self.user_short_password = {
            'email' : 'tester@mail.com',
            'username' : 'tester',
            'password' : 'te',
            'password2' : 'te',            
            'fullname' : 'testerfull',
        }
        self.user_unmatch_password = {
            'email' : 'tester@mail.com',
            'username' : 'tester',
            'password' : 'te',
            'password2' : 'te',            
            'fullname' : 'testerfull',
        }
        return super().setUp()

class RegisterTest(BaseTest):
    #Test register page loads properly
    def test_page_load(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/registration_form.html')
    
    #Test user can register
    def test_user_can_register(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)
    
    #Test user can't register with a short-password
    def test_user_short_password(self):
        response=self.client.post(self.register_url,self.user_short_password,format='text/html')
        self.assertEqual(response.status_code,200)

    #Test user can't register with a unmatching-passwords
    def test_user_unmatch_passwords(self):
        response=self.client.post(self.register_url,self.user_unmatch_password,format='text/html')
        self.assertEqual(response.status_code,200)

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
    def test_delete_contact(self):
        self.delete()
