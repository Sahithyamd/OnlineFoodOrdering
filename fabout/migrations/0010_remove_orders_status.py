# Generated by Django 3.0.2 on 2020-05-15 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabout', '0009_auto_20200515_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
    ]
