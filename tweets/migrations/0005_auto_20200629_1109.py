# Generated by Django 3.0.6 on 2020-06-29 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_date_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date_time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
