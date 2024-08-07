# Generated by Django 5.0.7 on 2024-07-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_property_bathrooms_alter_property_bedrooms_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='property',
            name='square_footage',
        ),
        migrations.RemoveField(
            model_name='property',
            name='year_built',
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='land_size',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
