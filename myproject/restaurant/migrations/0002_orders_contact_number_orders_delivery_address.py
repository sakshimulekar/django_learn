# Generated by Django 4.2.4 on 2023-08-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='contact_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]