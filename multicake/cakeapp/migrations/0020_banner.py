# Generated by Django 3.2 on 2022-03-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0019_alter_caketype_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Banner', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Bannerlar',
            },
        ),
    ]