# Generated by Django 4.2.3 on 2024-02-09 07:14

import django.db.models.deletion
from django.db import migrations, models

import core.enums


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FederationEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "projects_create",
                    models.BooleanField(
                        default=False,
                        verbose_name="Можно создавать авторские проекты",
                    ),
                ),
                (
                    "wiki_link",
                    models.URLField(
                        blank=True,
                        null=True,
                        verbose_name="Ссылка на статью на Википедии",
                    ),
                ),
                (
                    "has_subregions",
                    models.BooleanField(
                        default=False, verbose_name="Имеет субрегионы"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=core.enums.Limits["MAX_LENGTH_FIRST_NAME"],
                        unique=True,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "index",
                    models.IntegerField(
                        db_index=True,
                        unique=True,
                        verbose_name="Номер Субъекта",
                    ),
                ),
                (
                    "emblem",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="f_entities_emblems",
                        verbose_name="Герб региона",
                    ),
                ),
            ],
            options={
                "verbose_name": "Субъект Федерации",
                "verbose_name_plural": "Субъекты Федерации",
                "ordering": ["index"],
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "projects_create",
                    models.BooleanField(
                        default=False,
                        verbose_name="Можно создавать авторские проекты",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=core.enums.Limits["MAX_LENGTH_FIRST_NAME"],
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "wiki_link",
                    models.URLField(
                        blank=True,
                        null=True,
                        verbose_name="Ссылка на статью на Википедии",
                    ),
                ),
                (
                    "has_subregions",
                    models.BooleanField(
                        default=False, verbose_name="Имеет субрегионы"
                    ),
                ),
                (
                    "federation_entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="regions",
                        to="locations.federationentity",
                    ),
                ),
            ],
            options={
                "verbose_name": "Район",
                "verbose_name_plural": "Районы",
            },
        ),
        migrations.CreateModel(
            name="Settlement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=core.enums.Limits["MAX_LENGTH_FIRST_NAME"],
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "wiki_link",
                    models.URLField(
                        blank=True,
                        null=True,
                        verbose_name="Ссылка на статью на Википедии",
                    ),
                ),
                (
                    "has_subregions",
                    models.BooleanField(
                        default=False, verbose_name="Имеет субрегионы"
                    ),
                ),
                (
                    "projects_create",
                    models.BooleanField(
                        default=True,
                        verbose_name="Можно создавать авторские проекты",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="settlements",
                        to="locations.region",
                    ),
                ),
            ],
            options={
                "verbose_name": "Населенный пункт",
                "verbose_name_plural": "Населенные пункты",
            },
        ),
    ]
