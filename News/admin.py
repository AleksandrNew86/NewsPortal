from django.contrib import admin
from .models import Post, Author, Category
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'rating_author']
    list_filter = ['author']
    search_fields = ['author']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'type_post', 'date_creation', 'title_post']
    list_filter = ['author']
    search_fields = ['author']


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)

