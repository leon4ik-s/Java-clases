from django.contrib import admin
from .models import MilitaryUnit, Doctor, DoctorApplication

# Регистрация моделей в админке
admin.site.register(MilitaryUnit)
admin.site.register(Doctor)
admin.site.register(DoctorApplication)