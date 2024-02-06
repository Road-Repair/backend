from factory import fuzzy
from factory.django import DjangoModelFactory

from core.choices_classes import WorkTypes
from core.enums import Limits
from projects.models import Project


class ProjectFactory(DjangoModelFactory):
    number = fuzzy.FuzzyText(
        prefix="project_", length=Limits.MAX_LENGTH_PROJECT_DESCRIPTION
    )
    address = fuzzy.FuzzyText(
        prefix="address_", length=Limits.MAX_LENGTH_PROJECT_ADDRESS
    )
    work_type = fuzzy.FuzzyChoice(
        choices=WorkTypes.choices
    )

    class Meta:
        model = Project
