# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=20, blank=True)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('authors', models.ManyToManyField(related_name='author', to='main.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Corrigendum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('reason', models.CharField(max_length=200)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(to='main.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=60, blank=True)),
                ('state_province', models.CharField(max_length=30, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='main.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='translators',
            field=models.ManyToManyField(related_name='translator', to='main.Author', blank=True),
        ),
    ]
