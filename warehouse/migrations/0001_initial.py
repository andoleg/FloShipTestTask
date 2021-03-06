# Generated by Django 3.1.6 on 2021-02-07 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=25, verbose_name='URL')),
                ('name', models.CharField(max_length=25)),
                ('server_token', models.CharField(blank=True, max_length=25)),
                ('client_token', models.CharField(blank=True, default='', max_length=25)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=6, verbose_name='Order number')),
                ('status', models.CharField(
                    choices=[('New', 'new'), ('In progress', 'in progress'), ('Stored', 'stored'), ('Sent', 'sent')],
                    default='New', max_length=15)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='warehouse.store')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'abstract': False,
            },
        ),
    ]
