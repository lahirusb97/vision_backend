# Generated by Django 4.2.16 on 2025-01-31 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_lens_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='refractiondetails',
            name='is_manual',
            field=models.BooleanField(default=False),
        ),
    ]
