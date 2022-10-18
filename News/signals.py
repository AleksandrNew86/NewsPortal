from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post
from .tasks import notify_new_post_task


@receiver(m2m_changed, sender=Post.category_post.through)
def notify_new_post(sender, instance, action, **kwargs):
    title_post = instance.title_post
    notify_new_post_task.apply_async([title_post], countdown=1)
    return
