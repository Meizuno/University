from django.db import models
from authorization.models import User


class Subject(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    credits = models.IntegerField()
    students = models.ManyToManyField(
        User,
        through="StudentSubject",
        related_name="subjects",
    )
    guarantor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subject",
    )
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "subject"


class Room(models.Model):
    number = models.IntegerField(unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "room"


class ActivityType(models.Model):
    notation = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "activity_type"


class Activity(models.Model):
    annotation = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    students = models.ManyToManyField(
        User,
        through="StudentActivity",
        related_name="activities",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="activity",
    )
    date_time = models.DateTimeField(null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="activity")
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="activity")

    class Meta:
        db_table = "activity"
        unique_together = (("date_time", "room"), ("date_time", "instructor"))


class StudentActivity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_activity"
        unique_together = ("student", "activity")


class StudentSubject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        db_table = "student_subject"
        unique_together = ("student", "subject")
