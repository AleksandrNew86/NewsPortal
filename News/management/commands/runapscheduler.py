import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from News.models import Post, Category
from django.core.mail import send_mail
from django.template.loader import render_to_string
import datetime

logger = logging.getLogger(__name__)


def my_job():
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


def delete_old_job_executions(max_age=604860):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(week="01"),
            # То же, что и интервал, но задача тригера таким образом более понятна django
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                week="01", second="05"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
