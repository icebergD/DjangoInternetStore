# Generated by Django 3.2.9 on 2022-01-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20220114_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Цена'),
        ),
    ]
