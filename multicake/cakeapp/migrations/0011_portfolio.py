# Generated by Django 3.2 on 2022-02-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0010_auto_20220227_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Biznig ishlar', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Bizning ish',
                'verbose_name_plural': 'Bizning ishlar',
            },
        ),
    ]
