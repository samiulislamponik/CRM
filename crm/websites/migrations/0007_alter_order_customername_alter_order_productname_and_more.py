# Generated by Django 4.0 on 2022-02-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0006_alter_order_productquantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customerName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websites.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='productName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websites.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categoryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websites.product_category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paidAmount', models.FloatField(default=0)),
                ('paymentAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('paymentWay', models.CharField(choices=[('Cash', 'Cash'), ('MobileBanking', 'MobileBanking'), ('Banking', 'Banking')], default='None', max_length=100)),
                ('orderId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websites.order')),
            ],
        ),
    ]
