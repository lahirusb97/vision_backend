# Generated by Django 4.2.16 on 2024-12-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
