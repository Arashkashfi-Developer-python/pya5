# Generated by Django 5.1.2 on 2024-11-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_dataset_name_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='user',
        ),
    ]