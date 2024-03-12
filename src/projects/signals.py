from django.db.models.signals import post_save
from django.dispatch import receiver

from projects.models import Project, ProjectStatus


@receiver(post_save, sender=Project)
def create_account(sender, instance, created, **kwargs):
    """
    Создание записи о статусе проекта после создания проекта.
    """

    if created:
        ProjectStatus.objects.create(
            project=instance,
        )
