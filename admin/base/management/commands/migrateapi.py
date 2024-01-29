import os

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        os.system("python3 manage.py makemigrations --name fake_users users")
        os.system("python3 manage.py makemigrations --name fake_files files")
        os.system("python3 manage.py migrate --fake files 0003")
        # os.system("python3 manage.py migrate --fake files 0002")
