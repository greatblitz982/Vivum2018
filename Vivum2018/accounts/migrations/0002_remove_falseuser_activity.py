# Generated by Django 2.1 on 2018-08-23 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='falseuser',
            name='activity',
        ),
    ]
