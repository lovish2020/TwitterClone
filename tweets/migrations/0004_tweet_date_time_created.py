# Generated by Django 3.0.6 on 2020-06-29 05:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='date_time_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
