# Generated by Django 3.0.2 on 2020-01-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200128_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='nav_details',
            name='usr',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
