# Generated by Django 3.2 on 2022-02-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CakeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': "To'rt turi",
                'verbose_name_plural': "To'rt turlari",
            },
        ),
    ]
