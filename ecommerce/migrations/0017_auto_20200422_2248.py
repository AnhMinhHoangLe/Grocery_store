# Generated by Django 3.0.4 on 2020-04-23 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_contact_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='lastName',
        ),
    ]
