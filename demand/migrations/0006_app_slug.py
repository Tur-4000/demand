# Generated by Django 2.1.4 on 2018-12-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0005_auto_20181223_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='slug',
            field=models.SlugField(default='application', max_length=140),
        ),
    ]
