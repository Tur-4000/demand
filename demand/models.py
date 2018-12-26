from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from .utils import slugify

User = get_user_model()


class App(models.Model):
    """Приложения к которым выставляются требования
    """
    title = models.CharField(max_length=140,
                             verbose_name='Приложение',
                             db_index=True,
                             blank=False)
    slug = models.SlugField(max_length=140,
                            db_index=True,
                            blank=True,
                            null=True,
                            unique=True)

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Demand(models.Model):
    """Требования
    """
    PUTASIDE = 1
    COMPLETE = 2
    AWAIT = 3
    OPERATING = 4

    STATUS = (
        (PUTASIDE, 'Отложен'),
        (COMPLETE, 'Завершён'),
        (AWAIT, 'Не начат'),
        (OPERATING, 'В работе')
    )
    PRIORITY = (
        (1, 'Нужно вчера'),
        (2, 'Надо сделать'),
        (3, 'Хотелки'),
    )
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(verbose_name="Наименование",
                             max_length=250,
                             db_index=True,
                             blank=False)
    for_apps = models.ManyToManyField(App, verbose_name='Приложения')
    priority = models.PositiveSmallIntegerField(choices=PRIORITY,
                                                verbose_name='Приоритет',
                                                default=3)
    description = models.TextField(verbose_name='Описание',
                                   blank=False)
    status = models.PositiveSmallIntegerField(choices=STATUS,
                                              verbose_name='Статус',
                                              db_index=True,
                                              blank=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True, null=True, blank=True)
    last_edited = models.DateTimeField('Последнее редактирование', auto_now=True)
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено', db_index=True)

    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('demand_detail', kwargs={'pk': self.id})


class Comments(models.Model):
    """Комментарии
    """
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.DO_NOTHING,
                             null=True)
    demand = models.ForeignKey(Demand,
                               verbose_name='Требование',
                               on_delete=models.CASCADE,
                               null=True)
    text = models.TextField('Комментарий', null=True, blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '{}'.format(self.user)

