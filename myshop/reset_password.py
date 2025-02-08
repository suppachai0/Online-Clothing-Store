from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Reset user password'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('new_password', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        new_password = kwargs['new_password']
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Password for "{username}" has been reset.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist.'))