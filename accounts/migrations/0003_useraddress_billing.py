# Generated by Django 3.0.4 on 2020-04-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='billing',
            field=models.BooleanField(default=False),
        ),
    ]
