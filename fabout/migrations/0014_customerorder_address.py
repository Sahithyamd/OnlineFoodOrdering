# Generated by Django 3.0.2 on 2020-05-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabout', '0013_orders_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='address',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
