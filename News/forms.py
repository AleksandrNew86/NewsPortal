from django import forms
from .models import Post
from django.core.validators import ValidationError

from django.utils.translation import gettext_lazy as _


forbid_words = ['нех', 'пох']


class NewsForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'category_post', 'title_post', 'text_post']
        labels = {
            'category_post': _("Category"),
            'author': _('Athour'),
            'title_post': _('Title'),
            'text_post': _('Text'),
        }
        empty_labels = {
            'text_post': Post.text_post
        }

    def clean(self):
        clean_data = super().clean()
        title_post = clean_data.get('title_post')
        text_post = clean_data.get('text_post')
        for i in forbid_words:
            if i in title_post.lower():
                raise ValidationError(f'Название не может содержать слово {i}!')
            if i in text_post.lower():
                raise ValidationError(f'Текст не может содержать слово {i}!')
        return clean_data


