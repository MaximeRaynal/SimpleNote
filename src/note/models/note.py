import os
import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from note.models.page import Page

class Note(models.Model):
    """ Représentation d'une note comme un ensemble de page.

        La plus part des infos sont stocké de manière physique dans les
        dossiers le stockage en BDD sert à faciliter la recherche.

        Sur le disque une note est stocké dans le dossier settings.NOTE_DIR,
        à l'intérieur d'un dossier portant le nom de l'utilisateur.
        Une note est un dossier contenant les pages et les attachments.
        Le dossier est nommé nomNote_uuid
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    privacy_state = models.CharField(max_length=20)
    creation_date = models.DateTimeField()
    last_update = models.DateTimeField()
    is_crypted = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag', null=True)

    def __str__(self):
        return self.name

    def laod_page(self):
        """ Charge les pages (fichier stocké) associé à la note """
        note_directory = os.path.join(settings.NOTE_DIR, self.author)
        note_directory = os.path.join(note_directory, self.name)

        for element in note_directory:
            if element.endswith('.md'):
                self.pages.append(Page().load(element))

    def save(self):
        """ Enregistre la note sur le disque """
        passnote_directory = os.path.join(settings.NOTE_DIR, self.author)
        note_directory = os.path.join(passnote_directory, self.name + '_' + self.uuid)
        if not os.path.isdir(note_directory):
            os.mkdir(self.name)

        for page in self.pages:
            page_path = os.path.join(note_directory, page.__str__() + '.md')
            with open(page_path, 'w') as f:
                f.truncate()
                f.write(page.text)


