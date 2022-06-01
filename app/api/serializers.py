from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["pk", "email", "name"]


class WebhooksSerializer(serializers.ModelSerializer):
    """
    Serializer to support new incoming Webhooks with the capability of creating Patients
    """

    class Meta:
        model = Patient
        fields = ["email", "name"]
        validators = []
