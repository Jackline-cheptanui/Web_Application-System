from rest_framework import serializers
from rest_framework import viewsets
from Patient.models import Patient, Visit, Vital
from api.serializers import PatientSerializer, VisitSerializer, VitalSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class VitalViewSet(viewsets.ModelViewSet):
    queryset=Vital.objects.all()
    serializer_class=VitalSerializer
    
class VisitViewSet(viewsets.ModelViewSet):
    queryset=Visit.objects.all()
    serializer_class=VisitSerializer

