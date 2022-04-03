from rest_framework import mixins, viewsets

from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class WebhooksViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    This view provides receiving Webhooks integration to allow the creation of new Patients
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
