# Generated by Django 4.2.5 on 2023-09-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_coursegroup_groupmarks_student_subject_studentmark_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="professor",
            name="department",
        ),
        migrations.AddField(
            model_name="professor",
            name="subjects",
            field=models.ManyToManyField(to="api.subject"),
        ),
    ]
