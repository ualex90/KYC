import requests

from config import settings
from users.models import User


def create_admin_panel_user():
    """
    Автоматическое создание пользователя для админ панели

    Если данный пользователь не существует, он будет создан
    """
    if not User.objects.filter(email=settings.DJANGO_ADMIN_EMAIL):
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


def get_token():
    """
    Получение токена для авторизации в API
    """
    create_admin_panel_user()
    response = requests.post(
        url=f'{settings.API_URL}/api/auth/token/',
        json={
            'email': settings.DJANGO_ADMIN_EMAIL,
            'password': settings.DJANGO_ADMIN_PASSWORD,
        }
    )
    return response.json()
