# Generated by Django 3.0.4 on 2020-04-13 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_userstripeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdefaultaddress',
            name='billing',
        ),
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='shipping',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_default_address', to='accounts.UserAddress'),
        ),
    ]
