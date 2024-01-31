from django.core.management import BaseCommand

from config import settings
from users.models import User


class Command(BaseCommand):
    """
    Сброс пароля пользователя для админ панели
    """
    def handle(self, *args, **options):
        admin = User.objects.get(email=settings.DJANGO_ADMIN_EMAIL)
        admin.set_password(settings.DJANGO_ADMIN_PASSWORD)
        admin.save()
