# Generated by Django 2.1.4 on 2018-12-23 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0004_demand_is_delited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demand',
            old_name='is_delited',
            new_name='is_deleted',
        ),
    ]
