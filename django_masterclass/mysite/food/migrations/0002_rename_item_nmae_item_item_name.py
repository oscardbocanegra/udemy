# Generated by Django 3.2.8 on 2023-11-20 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_nmae',
            new_name='item_name',
        ),
    ]
