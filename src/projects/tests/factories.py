from factory import SubFactory, fuzzy
from factory.django import DjangoModelFactory

from core.choices_classes import WorkTypes
from core.enums import Limits
from projects.models import Project
from users.tests.factories import CustomUserFactory


class ProjectFactory(DjangoModelFactory):
    initiator = SubFactory(CustomUserFactory)
    number = fuzzy.FuzzyText(length=Limits.MAX_LENGTH_PROJECT_NUMBER.value)
    description = fuzzy.FuzzyText(
        length=Limits.MAX_LENGTH_PROJECT_DESCRIPTION.value
    )
    address = fuzzy.FuzzyText(length=Limits.MAX_LENGTH_PROJECT_ADDRESS.value)
    work_type = WorkTypes.LANDSCAPING

    class Meta:
        model = Project
