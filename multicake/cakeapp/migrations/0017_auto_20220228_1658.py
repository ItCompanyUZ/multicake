# Generated by Django 3.2 on 2022-02-28 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0016_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Buyurtma', 'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AddField(
            model_name='order',
            name='cake',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cakeapp.cake', verbose_name="To'rt"),
            preserve_default=False,
        ),
    ]
