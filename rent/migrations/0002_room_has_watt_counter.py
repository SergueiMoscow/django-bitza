# Generated by Django 5.0.3 on 2024-04-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='has_watt_counter',
            field=models.BooleanField(default=False, verbose_name='Есть электросчётчик'),
        ),
    ]