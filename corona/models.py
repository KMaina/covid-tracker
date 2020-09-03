from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False, blank=True)
    
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

#Patient treatment option
class Treatment(models.Model):
    treatment = models.CharField(max_length=100)

    def __str__(self):
        return self.treatment

    @classmethod
    def get_treatment_default(cls,treatment_default):
        treatment = Treatment.filter(treatment__icontains=treatment_default)        
        return treatment

class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

    @classmethod
    def get_statement_default(cls,status_default):
        status = Status.filter(status__icontains=status_default)        
        return status.id

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                
    name = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    phone = models.CharField(max_length=10) 
    prof_pic = models.ImageField(upload_to = 'doctor/', blank=True) 
    post_date = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.prof_pic and hasattr(self.prof_pic, 'url'):
            return self.prof_pic.url

    def save_doctor(self):
        self.save()

    @classmethod
    def get_doc_profile(cls, id):
        profiles = Doctor.objects.filter(user=id)
        profile = profiles.order_by("-post_date").first()
        return profile

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10) 
    location = models.CharField(max_length=10) 
    prof_pic = models.ImageField(upload_to = 'patient/', blank=True, null=True) 
    post_date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.prof_pic and hasattr(self.prof_pic, 'url'):
            return self.prof_pic.url
    
    @classmethod
    def get_pat_profile(cls, id):
        profiles = Patient.objects.filter(user=id)
        profile = profiles.order_by("-post_date").first()
        return profile

#Doctor report on a patient
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                
    comments = HTMLField(blank= True)
    temp = models.IntegerField()
    kit = models.CharField(max_length=100)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, blank=True)    
    treatment = models.ForeignKey(Treatment,on_delete=models.CASCADE, blank=True)    
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, blank=True) 
    post_date = models.DateTimeField(default=timezone.now)        

    def __str__(self):
        return self.user

    @classmethod
    def get_report(cls,id):
        reports = Report.objects.filter(user=id)
        report = reports.order_by("-post_date").first()
        return report

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    location = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()
