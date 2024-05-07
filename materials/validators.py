from rest_framework.serializers import ValidationError

word = "youtube.com"


def validate_youtube(value):
    if word not in value.lower():
        raise ValidationError("Некорректная ссылка")
