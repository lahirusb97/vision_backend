# Generated by Django 4.2.16 on 2024-12-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_full_name', models.CharField(max_length=255)),
                ('customer_mobile', models.CharField(max_length=15)),
                ('refraction_number', models.CharField(blank=True, max_length=10, unique=True)),
            ],
        ),
    ]
