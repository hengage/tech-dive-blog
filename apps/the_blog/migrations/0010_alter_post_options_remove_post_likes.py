# Generated by Django 4.1.2 on 2022-11-09 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0009_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
