from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    location = models.CharField(max_length=25)

    def _str_(self):
        return self.name

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()