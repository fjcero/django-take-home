from django.urls import include, path
from rest_framework import routers

from .views import PatientViewSet, WebhooksViewSet

router = routers.DefaultRouter()
router.register(r"patient", PatientViewSet)
router.register(r"ehr_webhook", WebhooksViewSet, basename="ehr_webhook")

urlpatterns = [
    path("", include(router.urls)),
]
