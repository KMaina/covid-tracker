from django.contrib import admin
from .models import Profile, Treatment ,Status, Report

# Register your models here.
admin.site.register(Profile)
admin.site.register(Treatment)
admin.site.register(Status)
admin.site.register(Report)