# Generated by Django 5.0.4 on 2024-05-08 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_passanger_flights'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passanger',
            new_name='Passenger',
        ),
    ]
