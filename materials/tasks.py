from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from materials.models import Course


@shared_task
def send_info_about_update(course_id):
    course = Course.objects.get(pk=course_id)
    sub_list = course.subscription.all()
    for sub in sub_list:
        send_mail('Есть обновление', 'Курс был обновлен!', EMAIL_HOST_USER,
                  [sub.user.email],)
