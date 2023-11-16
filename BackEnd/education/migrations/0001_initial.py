# Generated by Django 4.2.6 on 2023-11-16 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                ("guarantor_notes", models.CharField(max_length=255, null=True)),
                ("instructor_notes", models.CharField(max_length=255, null=True)),
                ("duration", models.IntegerField()),
                ("date_from", models.DateField()),
                ("date_to", models.DateField()),
                ("time", models.TimeField(null=True)),
                ("day", models.CharField(max_length=3, null=True)),
            ],
            options={
                "db_table": "activity",
            },
        ),
        migrations.CreateModel(
            name="ActivityRepetition",
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
                ("name", models.CharField(max_length=20, unique=True)),
            ],
            options={
                "db_table": "activity_repetition",
            },
        ),
        migrations.CreateModel(
            name="ActivityType",
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
                ("notation", models.CharField(max_length=5, unique=True)),
                ("name", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "activity_type",
            },
        ),
        migrations.CreateModel(
            name="InstructorSubject",
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
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "instructor_subject",
            },
        ),
        migrations.CreateModel(
            name="Room",
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
                ("number", models.IntegerField(unique=True)),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "room",
            },
        ),
        migrations.CreateModel(
            name="StudentSubject",
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
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "student_subject",
            },
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
                ("code", models.CharField(max_length=3, unique=True)),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255)),
                (
                    "guarantor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="guarantor_subject",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "instructors",
                    models.ManyToManyField(
                        related_name="instruktors_subjects",
                        through="education.InstructorSubject",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        related_name="student_subjects",
                        through="education.StudentSubject",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "subject",
            },
        ),
        migrations.AddField(
            model_name="studentsubject",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="education.subject"
            ),
        ),
        migrations.CreateModel(
            name="StudentActivity",
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
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="education.activity",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "student_activity",
                "unique_together": {("student", "activity")},
            },
        ),
        migrations.AddField(
            model_name="instructorsubject",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="education.subject"
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="activity_repetition",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="education.activityrepetition",
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="activity_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="education.activitytype"
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="instructor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="activity",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="activity",
                to="education.room",
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="students",
            field=models.ManyToManyField(
                related_name="student_activity",
                through="education.StudentActivity",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="activity",
                to="education.subject",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="studentsubject",
            unique_together={("student", "subject")},
        ),
        migrations.AlterUniqueTogether(
            name="instructorsubject",
            unique_together={("instructor", "subject")},
        ),
        migrations.AlterUniqueTogether(
            name="activity",
            unique_together={("day", "time", "room"), ("day", "time", "instructor")},
        ),
    ]
