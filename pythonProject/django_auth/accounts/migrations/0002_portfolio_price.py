# Generated by Django 5.0.1 on 2024-03-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]