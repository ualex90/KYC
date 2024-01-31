import requests

from config import settings


def get_token():
    """
    Получение токена для авторизации в API
    """
    response = requests.post(
        url=f'{settings.API_URL}/api/auth/token/',
        json={
            'email': settings.DJANGO_ADMIN_EMAIL,
            'password': settings.DJANGO_ADMIN_PASSWORD,
        }
    )
    return response.json()
