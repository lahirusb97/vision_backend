# Generated by Django 4.2.16 on 2024-12-27 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_order_refraction_alter_orderpayment_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RefractionDetails',
        ),
    ]
