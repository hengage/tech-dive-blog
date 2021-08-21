# Generated by Django 3.2.4 on 2021-07-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0003_auto_20210630_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='No category given', max_length=50),
        ),
    ]