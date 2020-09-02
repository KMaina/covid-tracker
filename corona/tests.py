from django.test import TestCase
from .models import *

# Create your tests here.
class TestContact(TestCase):
    def setUp(self):
        self.name = Contact(name='George')
        self.email = Contact(email='gkarumbi@gmail.com')
        self.phone = Contact(phone = '0722452772')
        self.location = Contact(location = 'Kigali')

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Contact))
        self.assertTrue(isinstance(self.email,Contact))
        self.assertTrue(isinstance(self.phone,Contact))
        self.assertTrue(isinstance(self.location, Contact))

    def test_save_contact(self):
        self.save()

    def test_delete_contact(self):
        self.delete()

from django.urls import reverse

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
        self.assertEqual(response.status_code,302)
    
    #Test user can't register with a short-password
    def test_user_short_password(self):
        response=self.client.post(self.register_url,self.user_short_password,format='text/html')
        self.assertEqual(response.status_code,302)

    #Test user can't register with a unmatching-passwords
    def test_user_unmatch_passwords(self):
        response=self.client.post(self.register_url,self.user_unmatch_password,format='text/html')
        self.assertEqual(response.status_code,302)

