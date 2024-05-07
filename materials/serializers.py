from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_youtube


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validate_youtube], read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lessons.count()
