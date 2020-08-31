from django.contrib import admin
from .models import User
from .models import Treatment ,Status, Report, Doctor,Patient

# Register your models here.
admin.site.register(User)
admin.site.register(Treatment)
admin.site.register(Status)
admin.site.register(Report)
admin.site.register(Patient)
admin.site.register(Doctor)

