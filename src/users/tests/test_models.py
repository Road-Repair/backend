from django.test import TestCase

from users.models import Account, CustomUser
from users.tests.factories import CustomUserFactory


class UsersModelsTest(TestCase):
    """Класс для тестирования моделей приложения users."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = CustomUserFactory()

    def test_user_creation(self):
        self.assertIsInstance(self.user, CustomUser)
        self.assertIsNotNone(self.user.pk)

    def test_account_association(self):
        account = Account.objects.get(user=self.user)
        self.assertIsInstance(account, Account)
        self.assertEqual(account.user, self.user)
