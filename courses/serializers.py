from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):

    trainer = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"]

