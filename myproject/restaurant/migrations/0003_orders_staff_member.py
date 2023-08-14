# Generated by Django 4.2.4 on 2023-08-14 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0002_orders_contact_number_orders_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='staff_member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
