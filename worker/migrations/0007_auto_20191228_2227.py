# Generated by Django 3.0.1 on 2019-12-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0006_auto_20191228_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]