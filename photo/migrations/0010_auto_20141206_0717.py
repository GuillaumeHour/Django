# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0009_auto_20141206_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='authors',
            field=models.ManyToManyField(to=b'photo.Author', blank=True),
        ),
    ]
