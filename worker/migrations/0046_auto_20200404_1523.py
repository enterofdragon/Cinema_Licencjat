# Generated by Django 3.0.4 on 2020-04-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0045_auto_20200404_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
