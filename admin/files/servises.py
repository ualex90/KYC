import requests

from base.servises import get_token
from config import settings


def file_change_status(queryset, status):
    """
    Изменение статуса файлов в API
    """
    for item in queryset:
        token = get_token()
        response = requests.post(
            url=f'{settings.API_URL}/api/files/status/{item.id}',
            params=f'status={status}',
            headers={'Authorization': F'{token.get("token_type")} {token.get("access_token")}'},
        )
        try:
            response.json()
        except requests.exceptions.RequestException:
            print("API error")
