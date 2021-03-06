# Generated by Django 2.0.1 on 2018-01-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_explorers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=1, to='books_explorers.Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
