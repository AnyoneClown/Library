# Generated by Django 4.1 on 2023-07-11 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_book_order_created_at_order_end_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='plated_end_at',
            new_name='planed_end_at',
        ),
    ]