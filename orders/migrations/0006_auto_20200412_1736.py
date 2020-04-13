# Generated by Django 3.0.4 on 2020-04-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200412_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Started', 'Started'), ('Pending', 'Pending'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='Started', max_length=120),
        ),
    ]
