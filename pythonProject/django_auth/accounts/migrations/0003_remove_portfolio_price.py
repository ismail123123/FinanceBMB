# Generated by Django 5.0.1 on 2024-03-18 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_portfolio_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='price',
        ),
    ]
