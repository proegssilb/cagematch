# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 05:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webPage', models.URLField(max_length=1024)),
                ('itemTitle', models.CharField(max_length=255)),
                ('itemText', models.TextField()),
                ('itemPicture', models.ImageField(upload_to='')),
                ('mu', models.FloatField(default=25.0, editable=False)),
                ('sigma', models.FloatField(default=8.333, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchTitle', models.CharField(max_length=255)),
                ('isPublic', models.BooleanField(default=False)),
                ('matchDescription', models.TextField()),
                ('matchPrompt', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Match'),
        ),
    ]
