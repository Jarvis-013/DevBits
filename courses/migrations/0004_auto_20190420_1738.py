# Generated by Django 2.2 on 2019-04-20 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190420_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 11, 38, 29, 822871, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 11, 38, 29, 822871, tzinfo=utc)),
        ),
    ]
