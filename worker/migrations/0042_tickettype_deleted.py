# Generated by Django 3.0.4 on 2020-04-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0041_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
