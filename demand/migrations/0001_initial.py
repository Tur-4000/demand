# Generated by Django 2.1.4 on 2018-12-20 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=140, verbose_name='Приложение')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=140, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Отложен'), (1, 'Завершён'), (2, 'Не начат'), (3, 'В работе')], db_index=True, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('last_edited', models.DateTimeField(auto_now=True, verbose_name='Последнее редактирование')),
                ('for_apps', models.ManyToManyField(to='demand.App', verbose_name='Приложения')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Требование',
                'verbose_name_plural': 'Требования',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='demand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demand.Demand', verbose_name='Требование'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
