# Generated by Django 4.2.5 on 2023-09-16 23:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseGroup",
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
                    "course_number",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Номер курса",
                    ),
                ),
                (
                    "group_number",
                    models.CharField(max_length=10, verbose_name="Номер группы"),
                ),
                (
                    "higher_education_level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("b", "bachelor"),
                            ("m", "magistracy"),
                            ("p", "postgraduate"),
                            ("s", "specialty"),
                        ],
                        max_length=1,
                        verbose_name="Ступень высшего образования",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GroupMarks",
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
                ("semester", models.IntegerField(verbose_name="Номер семестра")),
                (
                    "reporting_level",
                    models.CharField(
                        choices=[
                            ("t", "test"),
                            ("d", "differentiated test"),
                            ("e", "exam"),
                        ],
                        max_length=1,
                        verbose_name="Отчетность дисциплины",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.coursegroup",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                    "year_of_enrollment",
                    models.CharField(max_length=4, verbose_name="Год поступления"),
                ),
                (
                    "record_book_number",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Номер зачетной книжки"
                    ),
                ),
                (
                    "course_group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="student_group",
                        to="api.coursegroup",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
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
                    "name",
                    models.CharField(max_length=150, verbose_name="Навзвание предмета"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentMark",
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
                    "att1",
                    models.IntegerField(
                        null=True, verbose_name="Оценка за аттестацию 1"
                    ),
                ),
                (
                    "att2",
                    models.IntegerField(
                        null=True, verbose_name="Оценка за аттестацию 2"
                    ),
                ),
                (
                    "att3",
                    models.IntegerField(
                        null=True, verbose_name="Оценка за аттестацию 3"
                    ),
                ),
                (
                    "exam",
                    models.IntegerField(null=True, verbose_name="Оценка за экзамен"),
                ),
                (
                    "additional",
                    models.IntegerField(null=True, verbose_name="Дополнительные баллы"),
                ),
                (
                    "mark_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.groupmarks"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="api.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professor",
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
                ("department", models.CharField(max_length=50, verbose_name="Кафедра")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professor",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="groupmarks",
            name="professor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="api.professor"
            ),
        ),
        migrations.AddField(
            model_name="groupmarks",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="api.subject"
            ),
        ),
        migrations.CreateModel(
            name="Direction",
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
                    "name",
                    models.CharField(
                        max_length=50, verbose_name="Название направления"
                    ),
                ),
                (
                    "subjects",
                    models.ManyToManyField(related_name="directions", to="api.subject"),
                ),
            ],
        ),
    ]