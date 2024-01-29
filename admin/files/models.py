from django.db import models

from config import settings
from users.models import NULLABLE


class StatusFile(models.TextChoices):
    UNDER_REVIEW = 'under_review'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'


class File(models.Model):
    """ Модель файла """
    name = models.CharField(max_length=100, verbose_name='Имя файла')
    size = models.IntegerField(verbose_name='Размер файла')
    content_type = models.CharField(max_length=50, verbose_name='Тип файла')
    filename = models.CharField(max_length=30, unique=True, verbose_name='Имя файла на диске')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')
    status = models.CharField(
        max_length=12,
        choices=StatusFile,
        default=StatusFile.UNDER_REVIEW,
        verbose_name='Статус файла'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='files',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Владелец'
    )
    upload_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки файла')
    change_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения статуса')

    class Meta:
        db_table = "file"
