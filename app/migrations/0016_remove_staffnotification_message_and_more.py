# Generated by Django 4.1.4 on 2022-12-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_staff_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffnotification',
            name='message',
        ),
        migrations.AddField(
            model_name='staffnotification',
            name='staff_msg',
            field=models.TextField(blank=True, max_length=500, verbose_name='Write a message'),
        ),
    ]