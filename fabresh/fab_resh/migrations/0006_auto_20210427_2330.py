# Generated by Django 2.2 on 2021-04-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fab_resh', '0005_auto_20210427_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opros',
            name='start',
            field=models.CharField(default='2021-04-27 23:30:33', max_length=255),
        ),
    ]
