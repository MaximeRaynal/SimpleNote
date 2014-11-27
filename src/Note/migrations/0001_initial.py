# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('privacy_state', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('is_crypted', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('parent', models.ForeignKey(to='Note.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='Note.Tag'),
            preserve_default=True,
        ),
    ]
