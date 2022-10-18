
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task
from .models import Post, Category
import datetime

@shared_task
def notify_new_post_task(title_post):
    instance = Post.objects.latest('date_creation')
    if instance.title_post == title_post:
        subject = instance.title_post
        categories = instance.category_post.all()
        for category in categories:
            subscribers = category.subscribers.all()
            for subscriber in subscribers:
                if subscriber.email:
                    html_content = render_to_string(
                        'News/mail_message.html',
                        {
                            'post': instance,
                            'category': category,
                            'subscriber': subscriber,
                        },
                    )
                    send_mail(
                        subject=subject,
                        message=html_content,
                        from_email='seleznevaiu86@mail.ru',
                        recipient_list=[subscriber.email],
                        fail_silently=False,
                        html_message=html_content,
                    )

@shared_task
def send_every_week():
    time_now = (datetime.datetime.utcnow() - datetime.timedelta(7))
    posts = Post.objects.filter(date_creation__gte=time_now)
    categories = Category.objects.all()
    for category in categories:
        posts_cat = posts.filter(category_post=category)
        if posts_cat:
            subscribers = category.subscribers.all()
            mail = []
            for subscriber in subscribers:
                if subscriber.email:
                    mail.append(subscriber.email)
            html_content = render_to_string(
                'mail_message7day.html',
                {
                    'posts_cat': posts_cat,
                    'category': category,
                },
            )
            send_mail(
                subject='Новые статьи из вашей любимой категории на портале "NewsPortal" за последнюю неделю',
                message=html_content,
                from_email='seleznevaiu86@mail.ru',
                recipient_list=mail,
                fail_silently=False,
                html_message=html_content,
            )