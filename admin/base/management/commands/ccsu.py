from django.core.management import BaseCommand

from config import settings
from users.models import User


class Command(BaseCommand):
    """
    Cоздание пользователя для админ панели
    """

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email=settings.DJANGO_ADMIN_EMAIL,
            first_name='Admin',
            last_name='Django',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password(settings.DJANGO_ADMIN_PASSWORD)
        user.save()
        print("Создан пользователь Django ADMIN")
