
from .models import Patient, Visit, Vital
from django.shortcuts import redirect, render
from.forms import PatientRegistrationForms

from.forms import VitalRegistrationForms ,VisitRegistrationForms
from .models import Patient

def register_patient(request):
    if request.method== "POST":
        form=PatientRegistrationForms(request.POST,request.FILES,)
        if form.is_valid():
         form.save()
         return redirect('patient_list')
        else:
            print(form.errors)
    else:
        form=PatientRegistrationForms()
    return render(request,"register_patient.html",{"form":form})

def patient_list(request):
    patients=Patient.objects.all()
    return render(request,"patient_list.html",{"patients":patients})  

def vital_register(request):
    if request.method== "POST":
        form=VitalRegistrationForms(request.POST,request.FILES,)
        if form.is_valid():
         form.save()
         return redirect('vital_list')
        else:
            print(form.errors)
    else:
        form=VitalRegistrationForms()
        return render(request,"vital_register.html",{"form":form})
    

def vital_list(request):
    vitals=Vital.objects.all()
    return render(request,"vital_list.html",{"vitals":vitals}) 

def visit_list(request):
    visits=Visit.objects.all()
    return render(request,"visit_list.html",{"visits":visits})  


def visit_register(request):
    if request.method== "POST":
        form=VisitRegistrationForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
        else:
            print(form.errors)
    else:
        form=VisitRegistrationForms()
    return render(request,"visit_register.html", {"form":form})





# def bmi(request):
#     height=request.POST.get(height)
#     weight=request.POST.get(weight)
#     weight=float(weight)
#     height=float(height)
#     BMI = weight/(height*height)
#     weight=str(weight)
#     height=str(height)
#     BMI=str(BMI)
 
#     return HttpResponse({"Your Height = + height + meter + Your Weight =+ weight + KG + Your BMI = + BMI" })


