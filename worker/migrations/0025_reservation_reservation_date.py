# Generated by Django 3.0.1 on 2020-02-20 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0024_auto_20200215_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 21, 14, 26, 607937)),
        ),
    ]
