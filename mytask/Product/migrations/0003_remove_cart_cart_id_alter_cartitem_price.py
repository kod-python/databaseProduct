# Generated by Django 4.1.3 on 2024-06-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_cart_cart_id_cartitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
