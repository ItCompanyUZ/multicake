# Generated by Django 3.2 on 2022-02-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0008_filling'),
    ]

    operations = [
        migrations.AddField(
            model_name='filling',
            name='composition_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Tarkibi'),
        ),
        migrations.AddField(
            model_name='filling',
            name='composition_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Tarkibi'),
        ),
        migrations.AddField(
            model_name='filling',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='filling',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
    ]
