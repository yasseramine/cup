# Generated by Django 3.2.8 on 2021-11-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_orderlineitem_lineitem_delivery_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='postage',
            field=models.FloatField(default=0),
        ),
    ]
