import factory
from ..models import Patient


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient
    email = factory.Sequence(lambda n: 'user{}@example.com'.format(n))
    name = factory.Faker('first_name')
