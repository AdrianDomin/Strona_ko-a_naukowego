# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'album',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('album', models.ForeignKey(to='galeria.Album')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='photo',
            index_together=set([('id', 'slug')]),
        ),
    ]
