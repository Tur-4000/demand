from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class App(models.Model):
    title = models.CharField(max_length=140,
                             verbose_name='Приложение',
                             db_index=True,
                             blank=False)

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'

    def __str__(self):
        return self.title


class Demand(models.Model):
    """Требования
    """
    PUTASIDE = 0
    COMPLETE = 1
    AWAIT = 2
    OPERATING = 3

    STATUS = (
        (PUTASIDE, 'Отложен'),
        (COMPLETE, 'Завершён'),
        (AWAIT, 'Не начат'),
        (OPERATING, 'В работе')
    )

    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, default=1)
    title = models.CharField(verbose_name="Наименование",
                             max_length=140,
                             db_index=True,
                             blank=False)
    for_apps = models.ManyToManyField(App, verbose_name='Приложения')
    description = models.TextField(verbose_name='Описание',
                                   blank=False)
    status = models.PositiveSmallIntegerField(choices=STATUS,
                                              verbose_name='Статус',
                                              db_index=True,
                                              blank=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True, null=True, blank=True)
    last_edited = models.DateTimeField('Последнее редактирование', auto_now=True)

    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'
        ordering = ['id']

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Комментарии
    """
    pass
