# Generated by Django 3.0.2 on 2020-01-23 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20200123_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2020, 1, 23, 20, 2, 38, 571325, tzinfo=utc)),
        ),
    ]
