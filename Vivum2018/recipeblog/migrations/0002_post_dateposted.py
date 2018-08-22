# Generated by Django 2.1 on 2018-08-22 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datePosted',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published'),
            preserve_default=False,
        ),
    ]
