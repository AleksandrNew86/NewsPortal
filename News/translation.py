from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('name_category',)


@register(Post)
class PostTranslateOptions(TranslationOptions):
    fields = ('title_post', 'text_post')


