# Generated by Django 2.1.15 on 2021-05-02 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_history',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
