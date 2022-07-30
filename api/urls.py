from django.urls import path,include
from rest_framework import routers
from api.views import PatientViewSet, VisitViewSet, VitalViewSet


router=routers.DefaultRouter()
router.register("patients",PatientViewSet)
router.register("visits",VisitViewSet)
router.register("vitals",VitalViewSet)

urlpatterns=[
    path("",include(router.urls))
]