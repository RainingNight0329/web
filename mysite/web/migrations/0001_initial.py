# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 12:41
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=20)),
                ('intro', models.TextField(blank=True)),
                ('silver_coin', models.PositiveIntegerField(default=0)),
                ('gold_coin', models.PositiveIntegerField(default=0)),
                ('online_time', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('ucid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('upid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('classify', models.CharField(max_length=20)),
                ('click_times', models.DecimalField(decimal_places=0, max_digits=20)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('watched_time', models.DecimalField(decimal_places=0, max_digits=20)),
                ('like', models.DecimalField(decimal_places=0, max_digits=20)),
                ('dislike', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('uvid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='videoPhotos')),
                ('video_path', models.FileField(upload_to='videos')),
                ('content', models.TextField(blank=True)),
                ('classify', models.CharField(max_length=20)),
                ('click_times', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('vidoe_length', models.DecimalField(decimal_places=0, max_digits=20)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('watched_time', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('like', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('dislike', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Video'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Post'),
        ),
        migrations.AddField(
            model_name='account',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Comment'),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Post'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='account',
            name='videos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Video'),
        ),
    ]
