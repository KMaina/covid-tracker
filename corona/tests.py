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