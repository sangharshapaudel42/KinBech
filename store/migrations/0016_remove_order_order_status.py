# Generated by Django 3.1.4 on 2021-04-20 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_orderitem_orderitem_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
    ]
