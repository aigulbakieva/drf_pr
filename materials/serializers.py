from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
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

    def get_is_sub(self, course):
        user = self.context['request'].user
        subscription = Subscription.objects.filter(course=course.id, user=user.id)
        if subscription:
            return True
        return False
