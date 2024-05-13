from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    preview = models.ImageField(
        upload_to="materials/previews", verbose_name="Картинка", blank=True, null=True
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", null=True, blank=True)
    preview = models.ImageField(
        upload_to="materials/previews", verbose_name="Картинка", blank=True, null=True
    )
    url = models.URLField(verbose_name="ссылка на видео", null=True, blank=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="курс",
        related_name="lessons",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Владелец')

    def __str__(self):
        return f"{self.title} курс: {self.course}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='Пользователь',
                             on_delete=models.CASCADE, related_name='subscription')
    course = models.ForeignKey(Course, null=True, blank=True, verbose_name="Курс", on_delete=models.CASCADE,
                               related_name='subscription')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
