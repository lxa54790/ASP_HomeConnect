# Generated by Django 5.0.7 on 2024-07-28 23:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_rename_address_customuser_office_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
