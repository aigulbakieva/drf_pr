from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(email='aigul@sky.pro')
        paid_course = Course.objects.create(title='Python')
        paid_lesson = Lesson.objects.create(title='Django ORM')
        payments = [
            {
                'user': user,
                'payment_date': '2024-04-28',
                'paid_course': paid_course,
                'paid_lesson': paid_lesson,
                'payment_amount': '5000',
                'pay_method': 'card',
            }
        ]

        payment_list = []
        for payment in payments:
            payment_list.append(Payment(**payment))

        Payment.objects.bulk_create(payment_list)
