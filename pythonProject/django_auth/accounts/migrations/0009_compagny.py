# Generated by Django 5.0.2 on 2024-03-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_portfolio_costbasis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compagny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
