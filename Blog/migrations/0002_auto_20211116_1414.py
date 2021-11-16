# Generated by Django 3.2.8 on 2021-11-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='tilte',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
