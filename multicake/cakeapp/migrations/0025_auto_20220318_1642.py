# Generated by Django 3.2 on 2022-03-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0024_auto_20220318_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='adress_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Joylashuv manzili'),
        ),
        migrations.AddField(
            model_name='contact',
            name='adress_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Joylashuv manzili'),
        ),
    ]
