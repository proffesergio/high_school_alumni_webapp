# Generated by Django 4.1.4 on 2022-12-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alumni_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]