# Generated by Django 5.0.6 on 2024-10-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('cars', '0003_remove_car_brand_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ManyToManyField(to='brands.brand'),
        ),
    ]