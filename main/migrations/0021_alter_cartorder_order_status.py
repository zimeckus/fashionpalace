# Generated by Django 4.0.2 on 2022-04-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_productattribute_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='order_status',
            field=models.CharField(choices=[('OrderProcessed', 'OrderProcessed'), ('CashonDelivery', 'CashonDelivery'), ('OrderDelivered', 'OrderDelivered')], default='OrderProcessed', max_length=150),
        ),
    ]
