# Generated by Django 3.1.1 on 2020-09-08 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conctactApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='typeOfPerson',
            field=models.CharField(default='', max_length=36),
        ),
    ]