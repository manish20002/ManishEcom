# Generated by Django 3.2.8 on 2021-11-08 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_rename_item_json_orders_items_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='items_Json',
            new_name='items_json',
        ),
    ]
