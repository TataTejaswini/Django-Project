# Generated by Django 3.1.4 on 2021-01-06 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_market'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='cost',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='market',
            old_name='items',
            new_name='product',
        ),
    ]