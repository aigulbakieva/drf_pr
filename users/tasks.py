from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_last_user_login():
    today = timezone.now().today()
    max_days = today - timezone.timedelta(days=30)
    user_list = User.objects.filter(last_login__lt=max_days, is_active=True)
    user_list.update(is_active=False)

