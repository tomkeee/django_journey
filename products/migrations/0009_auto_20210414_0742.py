# Generated by Django 2.2.12 on 2021-04-14 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210414_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='summary',
        ),
    ]
