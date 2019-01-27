import string
from .models import Post, Subscribe
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery.task import periodic_task
from celery.beat import crontab
from django.utils import timezone
import datetime as DT
from django.template import context,Template
from django.core.mail import send_mail
from django.conf import settings


# @periodic_task(run_every=crontab(hour="8", minute="30", day_of_week="1"))
@periodic_task(run_every=DT.timedelta(seconds=30))
def send_post():
    print("start")
    # Post.objects.filter(published_date__gte=timezone.now().weekday('Monday')-7)
    posts = Post.published.filter(publish__date__gte=timezone.now().date() - DT.timedelta(days=7))
    post_content = {}
    for post in posts:
        post_content[post.title] = post.body
        # template = Template(create_email_data('path/to/your/email_template.html'))
        # Create your email html using Django's context processor
        # scheduled_report.save()
        recipients = Subscribe.objects.values_list("email", flat=True)
        print(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, recipients, "-----------------------------------")
        send_mail(
            subject='Test', message='Here is the message.',
            from_email=settings.EMAIL_HOST_USER, recipient_list=recipients,
            fail_silently=False, html_message=''
        )
    print("end")
    return
