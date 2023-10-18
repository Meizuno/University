from django.db import models
from authorization.models import User


class Subject(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=2, default='cz')
    credits = models.IntegerField()
    capacity = models.IntegerField()
    guarantor = models.ForeignKey(User, on_delete=models.PROTECT, related_name="garant_subject")  # think about restrict
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "subject"


class Activity(models.Model):
    annotation = models.CharField(max_length=255)
    duration = models.IntegerField()
    capacity = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_activity")

    class Meta:
        db_table = "activity"


class StudentActivity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_act")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="student_act")
    datetime = models.DateTimeField()

    class Meta:
        db_table = "studentActivity"


class StudentSubject(models.Model):
    passed = models.BooleanField(default=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_subject")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="student_subject")
    points = models.IntegerField()
    grade = models.CharField(max_length=1)

    class Meta:
        db_table = "studentSubject"


class Schedule(models.Model):
    scheduler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedule")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="schedule")
    datetime = models.DateTimeField()

    class Meta:
        db_table = "schedule"


class Room(models.Model):
    code = models.CharField(max_length=6, unique=True)
    capacity = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT, related_name="room")
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "room"


class InstructorRequest(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructor_request")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="instructor_request")
    datetime = models.DateTimeField()

    class Meta:
        db_table = "instructorRequest"


class InstructorActivity(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructor_activity")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="instructor_activity")
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "instructorActivity"

