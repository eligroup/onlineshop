# Generated by Django 4.2.2 on 2024-06-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_options_alter_orderitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_authority',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_ref_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
