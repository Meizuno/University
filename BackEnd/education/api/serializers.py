from rest_framework import serializers
from authorization.models import Permission, User
from education.models import Activity, ActivityType, Room, Subject
from django.core.validators import MinValueValidator, MaxValueValidator


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"


class ReadUserSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer()
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "permission",
        )


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    permission_id = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="ID of user's permission. \
            Get enum on 'api/auth/permissions/'",
    )


class ReadRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"


class RoomSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        validators=[
            MinValueValidator(100),
            MaxValueValidator(999),
        ]
    )
    description = serializers.CharField(required=False)


class ReadSubjectSerializer(serializers.ModelSerializer):
    guarantor = ReadUserSerializer()
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class ReadActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = "__all__"


class ReadActivitySerializer(serializers.ModelSerializer):
    subject = ReadSubjectSerializer()
    activity_type = ReadActivityTypeSerializer()
    room = ReadRoomSerializer()
    instructor = ReadUserSerializer()

    class Meta:
        model = Activity
        fields = "__all__"


class ActivityGuarantorSerializer(serializers.Serializer):
    guarantor_notes = serializers.CharField(
        max_length=255,
        required=False,
        allow_blank=True,
    )
    duration = serializers.IntegerField(validators=[MinValueValidator(1)])
    activity_type_id = serializers.IntegerField(
       help_text="ID of activity's type. \
           Get enum on 'api/auth/activity-type/'"
    )
    subject_id = serializers.IntegerField(
        help_text="ID of subject."
    )
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    activity_repetition_id = serializers.IntegerField(
       help_text="ID of activity's repetition. \
           Get enum on 'api/auth/activity-repetition/'"
    )


class ActivityInstructorSerializer(serializers.Serializer):
    instructor_id = serializers.IntegerField()


class ActivitySchedulerSerializer(serializers.Serializer):
    room_id = serializers.IntegerField(validators=[MinValueValidator(1)])
    time = serializers.TimeField(
        help_text="Format HH:MM"
    )
    day = serializers.CharField(max_length=3)


class RegisterInstructorSerializer(serializers.Serializer):
    instructor = serializers.IntegerField(validators=[MinValueValidator(1)])
    subject = serializers.IntegerField(validators=[MinValueValidator(1)])

