from django.urls import path
from education.api.views import *


urlpatterns = [
    # User's endpoints
    path("permission", get_permissions),
    path("user", get_users_or_create),
    path("user/<int:user_id>", rud_user),
    path("my-info", my_info),
    # Room's endpoints
    path("room", get_rooms_or_create),
    path("room/<int:room_id>", rud_room),
    # Subject's endpoints
    path("subject", get_subjects_or_create),
    path("subject/<int:subject_id>", rud_subject),
    # Student register subject
    path("register/<int:user_id>/<int:subject_id>", register_subject),
    # Activity
    path("activity", get_activity_or_create),
    path("activity/<int:activity_id>", delete_activity),
    path("activity/<int:activity_id>", get_activity),
    # Scheduler activity
    path("scheduler-activity/<int:activity_id>", add_activity_to_schedule),
    # Student subjects endpoint
    path("student_subjects/<int:student_id>", get_student_subjects),
    # Instructor register subject
    path("register_instructor/<int:instructor_id>/<int:subject_id>", register_instructor),
    # Instructor subject(s) endpoint
    path("instructor_subject/<int:instructor_id>", get_instructor_subject),
    # Get all instructos
    path("get_all_instructors", get_all_instructors),

]
