# Generated by Django 3.0.2 on 2020-05-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabout', '0008_orders_setsatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='setsatus',
            new_name='setstatus',
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('delivered', 'delivered'), ('on_the_way', 'on_the_way'), ('pending', 'pending')], default='pending', max_length=120),
        ),
    ]
