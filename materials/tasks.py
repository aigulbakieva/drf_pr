from celery import shared_task
from django.core.mail import send_mail
from config import settings
from materials.models import Course


@shared_task
def send_info_about_update(course_id):
    course = Course.objects.get(pk=course_id)
    sub_list = course.subscription.all()
    for sub in sub_list:
        send_mail(
            subject='Обновление',
            message=f'Курс {sub.course.title} был обновлен!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email],
        )
