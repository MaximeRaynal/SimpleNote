from django.core.management import BaseCommand

from simple_note_core.note_manager import NoteManager

from django.conf import settings

class Command(BaseCommand):

    help = "My test command"


    def handle(self, *args, **options):

        manager = NoteManager(settings.NOTE_DIR)

        manager.generate_meta('test')

        note = manager.load('test')

        note._pass()
        self.stdout.write('Done')