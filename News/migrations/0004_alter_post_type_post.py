# Generated by Django 4.0.6 on 2022-10-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_category_name_category_en_us_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type_post',
            field=models.CharField(choices=[('AR', 'Article'), ('NW', 'News')], default='AR', max_length=2),
        ),
    ]