# Generated by Django 3.1.4 on 2021-01-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210101_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=200)),
                ('cost', models.IntegerField(null=True)),
            ],
        ),
    ]
