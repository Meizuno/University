# Generated by Django 4.2.6 on 2023-10-19 10:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotation', models.CharField(max_length=255)),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='StudentSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student_subject',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(default='cz', max_length=2)),
                ('credits', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.CharField(max_length=255)),
                ('guarantor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='garant_subject', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(related_name='subjects', through='education.StudentSubject', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.AddField(
            model_name='studentsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.subject'),
        ),
        migrations.CreateModel(
            name='StudentActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.activity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student_activity',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='education.activity')),
                ('scheduler', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.CharField(max_length=255)),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room', to='education.schedule')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='InstructorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_request', to='education.activity')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_request', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'instructor_request',
            },
        ),
        migrations.CreateModel(
            name='InstructorActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_activity', to='education.activity')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_activity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'instructor_activity',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='students',
            field=models.ManyToManyField(related_name='activities', through='education.StudentActivity', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_activity', to='education.subject'),
        ),
    ]