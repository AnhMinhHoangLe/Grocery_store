# Generated by Django 3.0.4 on 2020-04-12 18:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_userdefaultsaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDefaultSAddress',
            new_name='UserDefaultAddress',
        ),
    ]
