from django.db import models
from authorization.models import User
from django.core.validators import MinValueValidator


class Subject(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=2, default='cz')
    credits = models.IntegerField(validators=[MinValueValidator(1)])
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    students = models.ManyToManyField(
        User,
        through="StudentSubject",
        related_name="subjects"
    )
    guarantor = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        related_name="garant_subject"
    )
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "subject"


class ActivityType(models.Model):
    notation = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "activity_type"


class Activity(models.Model):
    annotation = models.CharField(max_length=255)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    students = models.ManyToManyField(
        User,
        through="StudentActivity",
        related_name="activities"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="subject_activity"
    )

    class Meta:
        db_table = "activity"


class StudentActivity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    datetime = models.DateTimeField()

    class Meta:
        db_table = "student_activity"


class StudentSubject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        db_table = "student_subject"


class Schedule(models.Model):
    scheduler = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="schedule"
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="schedule"
    )
    datetime = models.DateTimeField()

    class Meta:
        db_table = "schedule"


class Room(models.Model):
    code = models.CharField(max_length=6, unique=True)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.SET_NULL,
        null=True,
        related_name="room"
    )
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "room"


class InstructorRequest(models.Model):
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="instructor_request"
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="instructor_request"
    )
    datetime = models.DateTimeField()

    class Meta:
        db_table = "instructor_request"


class InstructorActivity(models.Model):
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="instructor_activity"
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="instructor_activity"
    )
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "instructor_activity"

