# Generated by Django 3.2.4 on 2021-07-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210701_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='result',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]