# Generated by Django 5.1.2 on 2024-10-28 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_rename_tik_tikmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='tikmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.tikmodel'),
        ),
    ]
