from django.db import models


class Patient(models.Model):
    email = models.EmailField(max_length=250, blank=False, null=False)
    name = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        unique_together = (
            "email",
            "name",
        )
