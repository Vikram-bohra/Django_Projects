# Generated by Django 3.0.2 on 2020-01-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200128_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav_details',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
