<<<<<<< HEAD
from django.core.management.base import BaseCommand, CommandError
from News.models import Post, Category


class Command(BaseCommand, CommandError):
    help = "Введите комманду с указанием категории, статьи которой вы хотите удалить"
    missing_args_message = 'Не указана категория'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        # Positional arguments
=======
from django.core.management.base import CommandError, BaseCommand
from News.models import Post, Category

class Command(BaseCommand, CommandError):
    help = 'Команда удаляет все статьи указанной категори'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    missing_args_message = 'Не указана категория!'
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
>>>>>>> b126f1794bea1362072851dcb25a74ae4107aac2
        parser.add_argument('cat', help='имя категории')

    def handle(self, *args, **kwargs):
        cat = kwargs['cat']
<<<<<<< HEAD
        self.stdout.write(cat)
        category = Category.objects.filter(name_category=cat)
        category = category.first()
        self.stdout.write(category.name_category)
        if not category:
            raise CommandError(f'Category {cat} does not exist!')
        self.stdout.write(f'Do you really want to delete all posts in category {cat}? yes/no')
        answer = input()
        if answer == 'yes':  # в случае подтверждения действительно удаляем все посты данной категории
            posts_cat = category.post_set.all()
            for post in posts_cat:
                self.stdout.write(post.title_post)
                post.delete()
                post.save()
            self.stdout.write(self.style.SUCCESS(f'Succesfully wiped posts in category {cat}!'))
            return
        self.stdout.write(self.style.ERROR('Access denied'))
=======
        try:
            category = Category.objects.get(name_category=cat)
            self.stdout.write(f'Do you really want to delete all posts in category "{cat}"? yes/no')
            answer = input()
            if answer == 'yes':
                posts_cat = category.post_set.all()
                posts_cat.delete()
                self.stdout.write(self.style.SUCCESS('Succesfully wiped posts!'))
                return
            else:
                self.stdout.write(self.style.ERROR('Access denied'))
        except Category.DoesNotExist:
            self.stdout.write(f'Category "{cat}" does not exist')


>>>>>>> b126f1794bea1362072851dcb25a74ae4107aac2
