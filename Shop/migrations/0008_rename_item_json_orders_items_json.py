# Generated by Django 3.2.8 on 2021-11-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_rename_items_json_orders_item_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_Json',
            new_name='items_Json',
        ),
    ]
