# Generated by Django 5.1.4 on 2025-01-12 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0002_alter_meterreading_kwt_count'),
        ('rent', '0005_alter_payment_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meterreading',
            unique_together={('room', 'date')},
        ),
    ]
