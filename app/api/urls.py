from django.urls import include, path
from rest_framework import routers

from .views import PatientViewSet

router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet)

urlpatterns = [
    path('', include(router.urls))
]
