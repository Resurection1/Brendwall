from django.db import models

from api.constants import MAX_TITLE_LENGTH


class TestModels(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=MAX_TITLE_LENGTH
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Тестовое задание'
        verbose_name_plural = 'Тестовые задания'

    def __str__(self):
        return self.title[:MAX_TITLE_LENGTH]
