# Generated by Django 2.0.4 on 2018-04-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standup', '0003_auto_20180428_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='pivot',
            name='has_left_the_office',
            field=models.BooleanField(default=False),
        ),
    ]
