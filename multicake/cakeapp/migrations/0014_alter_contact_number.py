# Generated by Django 3.2 on 2022-02-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0013_alter_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=13, verbose_name='Telefon raqam'),
        ),
    ]
