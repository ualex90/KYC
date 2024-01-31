import requests

from base.servises import get_token
from config import settings


def file_change_status(queryset, status):
    """
    Изменение статуса файлов в API
    """
    token = get_token()
    for item in queryset:
        response = requests.post(
            url=f'{settings.API_URL}/api/files/status/{item.id}',
            params=f'status={status}',
            headers={'Authorization': F'{token.get("token_type")} {token.get("access_token")}'},
        )
        try:
            response.json()
        except requests.exceptions.RequestException:
            print("API error")
