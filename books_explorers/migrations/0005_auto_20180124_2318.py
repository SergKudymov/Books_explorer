# Generated by Django 2.0.1 on 2018-01-24 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_explorers', '0004_auto_20180124_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors_work',
            new_name='book_name',
        ),
    ]
