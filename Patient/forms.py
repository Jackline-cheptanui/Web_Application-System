
import datetime
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import HealthChoice, Patient, Visit, Vital,DietChoices


class DateInput(forms.DateInput):
        input_type = 'date'


class PatientRegistrationForms(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            'patient_number': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:99%'}),
            "registration_date": DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%', }),
            "date_of_birth": DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
            'gender': forms.Select(attrs={'class': 'form-select', 'style': 'width:99%'}),
        } 
        
    def __init__(self, *args, **kwargs):
        super(PatientRegistrationForms, self).__init__(*args, **kwargs)
        self.fields['registration_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        
class DateInput(forms.DateInput):
        input_type = 'date'
            
class VitalRegistrationForms(forms.ModelForm):
    class Meta:
        model = Vital
        fields = "__all__"
        widgets = {

            'patient_name': forms.TextInput(),
            'patient_visit_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
            'patient_height_in_center_metres': forms.NumberInput(),
            'patient_weight_in_kg':forms.NumberInput(),
        }
                
    def __init__(self, *args, **kwargs):
        super(VitalRegistrationForms, self).__init__(*args, **kwargs)
        self.fields['patient_visit_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        
        
        
class DateInput(forms.DateInput):
            input_type = 'date'
class VisitRegistrationForms(forms.ModelForm):
    class Meta:
        model=Visit
        fields= "__all__"
        widgets={
            'patient_name': forms.TextInput(),
            'visit_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
            'patient_general_health': forms.Select(choices=HealthChoice),
            'comments':forms.TextInput(),
            'weight_choice': forms.RadioSelect(choices=DietChoices,)
        }
                             
    def __init__(self, *args, **kwargs):
        super(VisitRegistrationForms, self).__init__(*args, **kwargs)
        self.fields['visit_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['patient_name']=forms.ModelChoiceField(queryset=Patient.objects.all())
        