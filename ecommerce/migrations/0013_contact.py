# Generated by Django 3.0.5 on 2020-04-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_contact', models.CharField(max_length=50)),
                ('last_name_contact', models.CharField(max_length=50)),
                ('email_contact', models.EmailField(max_length=254)),
                ('message_contact', models.TextField()),
            ],
        ),
    ]
