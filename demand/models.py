from django.db import models


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

    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'
        ordering = ['id']

    def __str__(self):
        return self.title
