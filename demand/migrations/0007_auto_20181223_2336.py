# Generated by Django 2.1.4 on 2018-12-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0006_app_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True),
        ),
    ]
