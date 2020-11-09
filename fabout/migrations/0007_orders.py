# Generated by Django 3.0.2 on 2020-05-14 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabout', '0006_remove_customerorder_userid1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120, unique=True)),
                ('status', models.CharField(choices=[('delivered', 'delivered'), ('pending', 'pending'), ('on_the_way', 'on_the_way')], default='pending', max_length=120)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fabout.CustomerOrder')),
            ],
        ),
    ]
