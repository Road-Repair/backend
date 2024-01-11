from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Account, CustomUser


@receiver(post_save, sender=CustomUser)
def create_account(sender, instance, created, **kwargs):
    """Создание аккаунта после создания юзера."""

    if created:
        Account.objects.create(
            user=instance,
        )
