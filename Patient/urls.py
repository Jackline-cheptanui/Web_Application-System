
from django.urls import path
from.views import register_patient
from.views import patient_list
from.views import vital_list
from.views import vital_register
from.views import visit_list
from.views import visit_register

urlpatterns = [
    path("register/",register_patient,name="register_patient"),
    path('list/',patient_list,name="patient_list"),
    path('vital_list/',vital_list,name="vital_list"),
    path('vital_register/',vital_register,name="vital_register"),
    path("visit_list/",visit_list,name="visit_list"),
    path("visit_register/",visit_register,name="visit_register"),
    
]
