# Generated by Django 2.2.2 on 2019-07-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190702_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]