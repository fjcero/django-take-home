from django.db import IntegrityError
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer, WebhooksSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class WebhooksViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    This view provides receiving Webhooks integration to allow the creation of new Patients
    """

    serializer_class = WebhooksSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except IntegrityError:
            """
            Ignore all Integrity Error expetions
            """
            pass

        return Response(serializer.data, status=status.HTTP_201_CREATED)
