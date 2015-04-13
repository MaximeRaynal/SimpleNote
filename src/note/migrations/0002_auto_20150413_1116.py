# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AddField(
            model_name='note',
            name='note_id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
    ]
