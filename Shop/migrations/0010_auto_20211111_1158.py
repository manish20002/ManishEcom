# Generated by Django 3.2.8 on 2021-11-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0009_rename_items_json_orders_items_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='items_json',
            new_name='items_Json',
        ),
    ]
