# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20190324_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTofollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('following', models.ManyToManyField(to='media.following')),
            ],
        ),
        migrations.DeleteModel(
            name='UserTofollo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='AlbumID',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='LocationId',
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ManyToManyField(to='media.photo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='tag',
            field=models.ManyToManyField(to='media.tag'),
        ),
        migrations.AddField(
            model_name='photo',
            name='Album',
            field=models.ManyToManyField(to='media.Album'),
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.ManyToManyField(to='media.location'),
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ManyToManyField(to='media.user'),
        ),
    ]