from django.db import models


class User(models.Model):
    """User model

    Model for users. have only name field. PK field ID django sets by default.

    """
    name = models.CharField('ФИО', max_length=255, null=False, )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
