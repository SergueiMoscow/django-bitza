# Generated by Django 4.1 on 2023-06-07 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_room_building'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-time'], 'verbose_name': 'Платёж', 'verbose_name_plural': 'Платежи'},
        ),
    ]
