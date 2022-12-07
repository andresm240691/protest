from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from protest import settings

@shared_task
def send_email_users():
    try:
        subject = "Test message"
        message = "Welcome. This is a celery test message"
        users = User.objects.all()
        for x in users:
            print("SEND EMAIL: {}".format(x.email))
            # send_mail(
            #     subject=subject,
            #     message=message,
            #     from_email=settings.EMAIL_HOST,
            #     fail_silently=False,
            #     recipient_list=[x.email]
            # )
    except Exception as e:
        print("Exception in send_email_users:" + str(e))