# Generated by Django 4.0 on 2022-02-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0005_alter_product_productprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='productQuantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.IntegerField(default=0),
        ),
    ]
