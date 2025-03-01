# Generated by Django 5.1.4 on 2025-02-20 21:26

import django.db.models.deletion
import rent.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0009_alter_contract_form_alter_contractprint_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractprint',
            name='form',
            field=models.ForeignKey(blank=True, default=rent.models.get_latest_contract_form, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.contractform', verbose_name='Бланк договора'),
        ),
    ]
