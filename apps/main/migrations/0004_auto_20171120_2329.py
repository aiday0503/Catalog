# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend_with',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.RemoveField(
            model_name='other',
            name='friends',
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_user_friends_+', to='main.User'),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='Other',
        ),
    ]