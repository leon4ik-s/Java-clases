from django.urls import path
from . import views
# military_units/urls.py
from .views import military_unit_list, doctor_list, doctor_application_list, humanitarian_aid_request_list

urlpatterns = [
    path('military-units/', military_unit_list, name='military_unit_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctor-applications/', doctor_application_list, name='doctor_application_list'),
    path('humanitarian-aid-requests/', humanitarian_aid_request_list, name='humanitarian_aid_request_list'),
]
