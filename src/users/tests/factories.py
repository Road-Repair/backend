from factory import Faker, LazyAttribute
from factory.django import DjangoModelFactory

from core.choices_classes import Role
from users.models import CustomUser


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = LazyAttribute(lambda o: f"{o.last_name}@example.org")
    phone = Faker("phone_number")
    role = Role.USER
    is_superuser = False
    is_active = True
