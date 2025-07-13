from django.core.management.base import BaseCommand

from notes.models import Note


class Command(BaseCommand):
    def handle(self, *args, **options):
        Note.objects.all().delete()
