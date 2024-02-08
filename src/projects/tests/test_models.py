from django.contrib.contenttypes.models import ContentType

from core.choices_classes import StatusOfProject
from core.fixtures import LocationsFixtures
from projects.models import Project, ProjectStatus
from projects.tests.factories import ProjectFactory


class ProjectsModelsTest(LocationsFixtures):
    """
    Класс для тестирования моделей приложения projects.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.project_1 = ProjectFactory(
            object_id=cls.settlement_1.id,
            content_type=ContentType.objects.get(
                app_label="locations", model="settlement"
            ),
            initiator=cls.user,
        )

    def test_project_creates(self):
        self.assertTrue(
            ProjectStatus.objects.filter(project=self.project_1).exists()
        )

    def test_models_have_correct_object_names(self):
        self.assertEqual(str(self.project_1), self.project_1.number)
        self.assertEqual(
            str(ProjectStatus.objects.get(project=self.project_1)),
            (
                f"Проект {self.project_1.number},"
                f" статус {StatusOfProject.CREATED}"
            ),
        )

    def test_models_default_values(self):
        self.assertFalse(self.project_1.needed_promotion)
        self.assertEqual(self.project_1.actual_status, StatusOfProject.CREATED)

    def test_models_methods(self):
        self.project_1.promote()
        self.assertTrue(
            Project.objects.get(id=self.project_1.id).needed_promotion
        )

        new_status = StatusOfProject.CONFIRMED
        self.project_1.change_status(new_status)
        self.assertEqual(
            Project.objects.get(id=self.project_1.id).actual_status, new_status
        )
        self.assertTrue(
            ProjectStatus.objects.filter(
                project=self.project_1, status=new_status
            ).exists()
        )
