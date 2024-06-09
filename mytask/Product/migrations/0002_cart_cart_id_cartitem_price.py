# Generated by Django 4.1.3 on 2024-06-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default=10, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
        ),
    ]