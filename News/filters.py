import django_filters
from .models import Post
from .choice import *
from django import forms
from django.utils.translation import gettext_lazy as _

class PostFilter(django_filters.FilterSet):
    type_post_filter = django_filters.ChoiceFilter(field_name='type_post',
                                                   choices=CHOICE_TYPE,
                                                   empty_label=_('Any type'),
                                                   label=_('Post type')
                                                   )
    title_post_filter = django_filters.CharFilter(field_name='title_post',
                                                  lookup_expr='icontains',
                                                  label=_('Title'))
    date_creation_filter = django_filters.DateFilter(field_name='date_creation',
                                                     lookup_expr='gt',
                                                     label=_('Publication date'),
                                                     widget=forms.DateInput(attrs={'type': 'date'})
                                                     )

    class Meta:
        model = Post
        fields = ['title_post_filter', 'type_post_filter', 'date_creation_filter']
