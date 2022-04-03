from rest_framework import status
from rest_framework.test import APITestCase
from .factories import PatientFactory

# Required to enable SkipTest
# import unittest


class APITest(APITestCase):
    def test_get_patient(self):
        patient_mocks = PatientFactory.create_batch(4)
        response = self.client.get("/patient/")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.json()), 4)

    def test_create_patient(self):
        # Create assertable responses
        error_response = self.client.post(
            "/patient/", data=dict(email="", name=""), format="json"
        )
        valid_response = self.client.post(
            "/patient/",
            data=dict(email="sally@floatfi.com", name="Sally Jones"),
            format="json",
        )
        self.assertEquals(error_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(valid_response.status_code, status.HTTP_201_CREATED)

    def test_ehr_webhook(self):
        error_case_payload = self.client.post(
            "/ehr_webhook/",
            data=dict(email="jane@example.com", name="Name"),
            format="json",
        )

        success_case_single = 201

        self.assertEquals(error_case_payload.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(success_case_single, status.HTTP_201_CREATED)
