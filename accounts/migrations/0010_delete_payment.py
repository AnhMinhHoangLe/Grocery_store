# Generated by Django 3.0.4 on 2020-04-12 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]