# Generated by Django 2.2 on 2021-04-27 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fab_resh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opros',
            name='start',
            field=models.CharField(default=datetime.datetime(2021, 4, 27, 23, 14, 22, 458590), max_length=255),
        ),
    ]
