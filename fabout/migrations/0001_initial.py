# Generated by Django 3.0.2 on 2020-04-29 10:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(default='0', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fabout.Item')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateField(default=datetime.datetime.now)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('items1', models.ManyToManyField(blank=True, null=True, to='fabout.ItemOrder')),
                ('products', models.ManyToManyField(blank=True, null=True, to='fabout.Item')),
            ],
        ),
    ]
