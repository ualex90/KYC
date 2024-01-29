from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя """
    email = models.CharField(max_length=255, unique=True, verbose_name='Email')
    username = models.CharField(max_length=150, **NULLABLE, verbose_name="НЕ ИСПОЛЬЗУЕТСЯ")
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, **NULLABLE, verbose_name='Отчество')
    is_active = models.BooleanField(default=True, verbose_name='Признак активности')
    comments = models.TextField(**NULLABLE, verbose_name='Информация о пользователе')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
