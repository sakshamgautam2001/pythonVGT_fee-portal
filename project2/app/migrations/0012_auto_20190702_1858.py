# Generated by Django 2.2.2 on 2019-07-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190702_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='name',
            field=models.TextField(default='no update', max_length=100),
        ),
        migrations.AddField(
            model_name='requests',
            name='new_email',
            field=models.TextField(default='no update', max_length=100),
        ),
        migrations.AddField(
            model_name='requests',
            name='roll_number',
            field=models.TextField(default='no update', max_length=100),
        ),
        migrations.AddField(
            model_name='requests',
            name='standard',
            field=models.TextField(default='no update', max_length=100),
        ),
    ]
