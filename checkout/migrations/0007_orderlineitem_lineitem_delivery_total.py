# Generated by Django 3.2.8 on 2021-11-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='lineitem_delivery_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
    ]