from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

from core.services import send_password_reset_token
from users.models import Account, CustomUser


@receiver(post_save, sender=CustomUser)
def create_account(sender, instance, created, **kwargs):
    """Создание аккаунта после создания юзера."""

    if created:
        Account.objects.create(
            user=instance,
        )


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """

    send_password_reset_token(reset_password_token)
