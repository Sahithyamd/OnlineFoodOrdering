# Generated by Django 3.0.2 on 2020-05-17 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fabout', '0012_auto_20200516_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='userid',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
