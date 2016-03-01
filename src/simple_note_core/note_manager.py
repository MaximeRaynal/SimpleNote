import re
import os
import json

from simple_note_core.note import NoteMeta
from simple_note_core.note import Note
from simple_note_core.note import SimpleNoteEncoder

class NoteManager(object):
    """
        Classe contenant tous les outils pour gérer les notes quel que soit
        l'application
    """

    FILE_EXTENSION = '.note_page'
    META_FILE_NAME = 'meta.json'

    def __init__(self, notes_folder):
        super(NoteManager, self).__init__()
        self.notes_folder = notes_folder

        self.check_notes_dir_exist()

    def check_notes_dir_exist(self):
        """
            Vérifie si le dossier de destination des notes existe
            sinon le crée
        """
        if not os.path.isdir(self.notes_folder):
            os.mkdir(self.notes_folder)

    def generate_meta(self, note_name):
        """
            Génère si besoin le fichier meta.json pour un dossier de notes
            Le fichier de note contient diverses informations sur les notes.
            C'est informations sont importante et/ou utile
            Les notes peuvent être lu sans, mais certaine information peuvent
            être perdu avec ce fichier (auteur / pagination)
            C'est informations peuvent être (mais pas seulement) :
                - l'auteur
                - la date de création
                - les références aux attachments
                - la pagination
        """

        note_folder = os.path.join(self.notes_folder, note_name)

        meta_file_name = os.path.join(note_folder, self.META_FILE_NAME)

        if os.path.isfile(meta_file_name):
            return NoteMeta.load_from_json(meta_file_name)

        file_list = os.listdir(note_folder)


        attachments = list()
        pages = list()

        for f in file_list:

            file_name = os.path.realpath(os.path.join(self.notes_folder, f))

            if os.path.isdir(file_name):
                print('Dossier trouvé : %s, comportement anormal', file_name)
            else:
                if self.is_page_name(file_name):
                    pages.add(file_name)
                else:
                    attachments.add(file_name)


        meta = NoteMeta()

        meta.pages = pages
        meta.attachments = attachments
        meta.folder_name = note_folder

        import ipdb; ipdb.set_trace()

        with open(meta_file_name, 'w') as meta_file:
            json.dump(meta, meta_file, cls=SimpleNoteEncoder)

        return meta

    def generate_all_meta(self):
        """
            Itère sur tous les dossiers de notes et
            appele la fonction generate_meta
        """
        pass

    def is_page_name(self, file_name):
        """
            Détermine si le fichier trouvé est une page ou si c'est une pièce
            jointe.
            Renvoi True si c'est une page
            Est une page tout fichier texte avec l'extension : .note_page
        """
        return file_name.endswith(self.FILE_EXTENSION)

    def load(self, note_name):
        note_folder = os.path.join(self.notes_folder, note_name)

        if not os.path.isdir(note_folder):
            raise NotADirectoryError('Pas de dossier au nom de la note')

        meta_file = os.path.join(note_folder, self.META_FILE_NAME)

        if not os.path.isfile(meta_file):
            self.generate_meta(note_name)

        meta = NoteMeta.load_from_json(meta_file)

        note = Note(meta)

        return note




