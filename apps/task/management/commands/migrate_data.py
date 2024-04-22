from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        instance, _ = User.objects.update_or_create(id=1, defaults={
            "username": "hamzakhalil",
            "email": "hamzakhalil@email.com",
        })
        print("User created" if _ is True else "User Updated")
