# Generated by Django 3.2 on 2022-03-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0021_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='price_for_kg',
            field=models.CharField(max_length=200, verbose_name='1 kg narxi'),
        ),
    ]
