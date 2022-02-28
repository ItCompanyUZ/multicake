# Generated by Django 3.2 on 2022-02-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0011_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Telefon raqam')),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontaktlar',
            },
        ),
    ]
