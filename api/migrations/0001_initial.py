# Generated by Django 4.2.5 on 2023-09-16 23:01

import api.models
import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=50,
                        unique=True,
                        validators=[api.validators.CustomUnicodeUsernameValidator()],
                        verbose_name="Логин",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=20, verbose_name="Имя"),
                ),
                (
                    "second_name",
                    models.CharField(blank=True, max_length=20, verbose_name="Фамилия"),
                ),
                (
                    "patronymic",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Отчество"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with that email already exists."
                        },
                        max_length=254,
                        unique=True,
                        verbose_name="Адрес электронной почты",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Аккаунт работника",
                        verbose_name="Стафф",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="Активный",
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(default=False, verbose_name="Подтвержденный"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", api.models.UserManager()),
            ],
        ),
    ]