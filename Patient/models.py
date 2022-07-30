import datetime
from django.db import models


class Patient(models.Model):
    patient_number=models.BigAutoField(primary_key=True,unique=True)
    registration_date=models.DateTimeField(null=True)
    first_name=models.CharField(max_length=17,null=True)
    last_name=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateTimeField()
    gender_choice=(
        ("male","Male"),
        ("female","Female"),
        ("other","Other"),
    )
    gender=models.CharField(max_length=17,choices=gender_choice,null=True)
    
    def __str__(self) :
        return (f'{self.first_name } {self.last_name}')
    
class Vital(models.Model):
    patient_name=models.CharField(max_length=15)
    patient_visit_date=models.DateTimeField(null=True)
    age=models.PositiveSmallIntegerField(null=True,default=20)
    patient_height_in_center_metres=models.IntegerField()
    patient_weight_in_kg=models.IntegerField()
    
    @property
    def patient_bmi(self):
        height = self.patient_height_in_center_metres/100
        bmi=self.patient_weight_in_kg/(height*height)
        return bmi
    
    
class DietChoices(models.TextChoices):
    YES="Yes",
    NO="No"



class HealthChoice(models.TextChoices):
        GOOD="Good",
        POOR="Poor"
        
class Visit(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE)
    visit_date=models.DateField()
    patient_general_health=models.CharField(max_length=17,choices=HealthChoice.choices,null=True)
    comments=models.CharField(max_length=500,null=True)
    weight_choice = models.CharField(max_length=17,choices=DietChoices.choices, default=DietChoices.NO)
    