from dataclasses import fields
from rest_framework import serializers
from Patient.models import Patient
from Patient.models import Visit
from Patient.models import Vital


from Patient.models import Vital,Visit

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'
        

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vital
        fields='__all__'
        
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields='__all__'
