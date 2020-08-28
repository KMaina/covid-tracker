from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)    
    phone = models.CharField(max_length=50)  
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, default=None)

    def __str__(self):
        return self.full_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
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

#Doctor report on a patient
class Report(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                
    comments = HTMLField(blank= True)
    temp = models.IntegerField()
    kit = models.CharField(max_length=100)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, blank=True)    
    treatment = models.ForeignKey(Treatment,on_delete=models.CASCADE, blank=True)    

    def __str__(self):
        return self.user

    @classmethod
    def get_report(cls,id):
        report = Report.objects.filter(user=id).first()
        return report
