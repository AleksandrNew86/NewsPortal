# Generated by Django 4.0.6 on 2022-10-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_category_en_us',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_category_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_post_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_post_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_post_en_us',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_post_ru',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
