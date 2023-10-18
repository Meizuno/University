from django.db import models
from django.contrib.postgres.fields import ArrayField


# class Permission(models.Model):
#     level = models.CharField(max_length=20)


# class User(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)  # think about cascade


class Subject(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=2, default='cz')
    credits = models.IntegerField()
    capacity = models.IntegerField()
    guarantor = models.ForeignKey(User, on_delete=models.RESTRICT)  # think about restrict
    description = models.CharField(max_length=255)


class Activity(models.Model):
    annotation = models.CharField(max_length=255)
    duration = models.IntegerField()
    capacity = models.IntegerField()
    #repeating = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class StudentActivity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    datetime = models.DateTimeField()


class StudentSubject(models.Model):
    passed = models.BooleanField(default=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    points = models.IntegerField()
    grade = models.CharField(max_length=1)  # not int?


class Schedule(models.Model):
    scheduler = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # ?????????????
    datetime = models.DateTimeField(auto_now_add=True)
    weeks = ArrayField(models.IntegerField())


class Room(models.Model):
    code = models.CharField(max_length=6)
    capacity = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.RESTRICT)
    description = models.CharField(max_length=255)


class ScheduleRequest(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    datetime = models.DateTimeField()


class InstructorActivity(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

