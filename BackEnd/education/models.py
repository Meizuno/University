from django.db import models
from authorization.models import User


class Subject(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(
        User,
        through="StudentSubject",
        related_name="student_subjects",
    )
    guarantor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="guarantor_subject",
    )
    instructors = models.ManyToManyField(
        User,
        through="InstructorSubject",
        related_name="instruktors_subjects",
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
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "activity_type"


class ActivityRepetition(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "activity_repetition"


class Activity(models.Model):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    activity_repetition = models.ForeignKey(ActivityRepetition, on_delete=models.PROTECT)
    guarantor_notes = models.CharField(max_length=255, null=True)
    instructor_notes = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()
    students = models.ManyToManyField(
        User,
        through="StudentActivity",
        related_name="student_activity",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="activity",
    )
    date_from = models.DateField()
    date_to = models.DateField()
    time = models.TimeField(null=True)
    day = models.CharField(max_length=3, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="activity")
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="activity")

    class Meta:
        db_table = "activity"
        unique_together = (("day", "time", "room"), ("day", "time", "instructor"))


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


class InstructorSubject(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        db_table = "instructor_subject"
        unique_together = ("instructor", "subject")
