# Generated by Django 4.2.17 on 2025-01-07 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_alter_booking_check_in_alter_booking_from_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 18, 16, 1, 237970)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='from_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 18, 16, 1, 237952)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='to_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 18, 16, 1, 237963)),
        ),
    ]
