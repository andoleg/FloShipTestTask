# Generated by Django 3.1.6 on 2021-02-04 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_num',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='status',
        ),
    ]
