from factory import Faker, LazyAttribute, PostGenerationMethodCall, Sequence
from factory.django import DjangoModelFactory

from core.choices_classes import Role
from users.models import CustomUser

PASSWORD = "SoMePaSS_word_123"


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = Sequence(lambda num: "user_{0}".format(num))
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = LazyAttribute(lambda o: f"{o.last_name}@example.org")
    phone = Sequence(lambda num: "+7900000000{0}".format(num))
    role = Role.USER
    is_superuser = False
    is_active = True
    password = PostGenerationMethodCall("set_password", PASSWORD)
