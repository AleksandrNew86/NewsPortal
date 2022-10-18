from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache
from .choice import *


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(result_p=Sum('rating_post')).get('result_p')
        if post_rating is None:
            post_rating = 0
        comment_rating = self.author.comment_set.aggregate(result_c=Sum('rating_comment')).get('result_c')
        if comment_rating is None:
            comment_rating = 0
        self.rating_author = post_rating * 3 + comment_rating
        self.save()

    def __str__(self):
        return f'{self.author.username}'


class Category(models.Model):
    name_category = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.name_category}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=CHOICE_TYPE, default=article)
    date_creation = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    title_post = models.CharField(max_length=64)
    text_post = models.TextField()
    rating_post = models.SmallIntegerField(default=0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[0:124] + '...'

    def __str__(self):
        return f'{self.title_post}'

    def get_absolute_url(self):
        return reverse('news_details', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating_comment = models.SmallIntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
