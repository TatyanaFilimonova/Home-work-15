# Generated by Django 3.2.8 on 2021-10-16 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_server', '0003_auto_20211016_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_header',
            new_name='header',
        ),
        migrations.AlterField(
            model_name='sports',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 10, 34, 50, 425248)),
        ),
    ]
