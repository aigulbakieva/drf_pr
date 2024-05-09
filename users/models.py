from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_CHOICE = [('cash', 'Наличные'), ('card', 'оплата картой')]
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, verbose_name='Оплаченный курс', on_delete=models.CASCADE, null=True,
                                    blank=True, related_name='payment')
    paid_lesson = models.ForeignKey(Lesson, verbose_name='Оплаченный урок', on_delete=models.CASCADE, null=True,
                                    blank=True, related_name='payment')
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    pay_method = models.CharField(max_length=50, verbose_name='Способ оплаты', choices=PAYMENT_CHOICE)
    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="ID сессии")
    link = models.URLField(max_length=400, blank=True, null=True, verbose_name="Ссылка на оплату")

    def __str__(self):
        return {self.user}, {self.payment_amount}

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
