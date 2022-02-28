# Generated by Django 3.2 on 2022-02-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0007_auto_20220226_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('composition', models.CharField(max_length=255, verbose_name='Tarkibi')),
                ('image', models.ImageField(upload_to='Nachinka/%Y/%m', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Nachinka',
                'verbose_name_plural': 'Nachinkalar',
            },
        ),
    ]
