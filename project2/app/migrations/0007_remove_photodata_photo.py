# Generated by Django 2.2.2 on 2019-07-01 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190701_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photodata',
            name='photo',
        ),
    ]