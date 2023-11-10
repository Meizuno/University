from django.db import models
from authorization.models import User


class Subject(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    credits = models.IntegerField()
    capacity = models.IntegerField()
    students = models.ManyToManyField(
        User,
        through="StudentSubject",
        related_name="subjects",
    )
    guarantor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="garant_subject",
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
    annotation = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()
    capacity = models.IntegerField()
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    students = models.ManyToManyField(
        User,
        through="StudentActivity",
        related_name="activities",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="subject_activity",
    )

    class Meta:
        db_table = "activity"


class StudentActivity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = "student_activity"
        unique_together = ("student", "activity")


class StudentSubject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        db_table = "student_subject"
        unique_together = ("student", "subject")


class Schedule(models.Model):
    scheduler = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="schedule",
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="schedule",
    )
    datetime = models.DateTimeField()

    class Meta:
        db_table = "schedule"
        unique_together = ("activity", "datetime")


class Room(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    schedule = models.ForeignKey(
        Schedule, on_delete=models.SET_NULL, null=True, related_name="room"
    )
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "room"


class InstructorRequest(models.Model):
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="instructor_request",
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="instructor_request",
    )
    datetime = models.DateTimeField()

    class Meta:
        db_table = "instructor_request"
        unique_together = ("activity", "datetime")


class InstructorActivity(models.Model):
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="instructor_activity",
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="instructor_activity",
    )
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "instructor_activity"
        unique_together = ("instructor", "activity")
