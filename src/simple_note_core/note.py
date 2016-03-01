import json
import re

class Note(object):
    """
        Représentation OO d'une Note
        Permet de facilement manipuler les objets
        Est instancié à partir d'un objet Meta
    """
    def __init__(self, meta):
        super(Note, self).__init__()
        self.meta = meta
        self.pages = meta.pages
        self.attachments = meta.attachments

    def _pass(self):
        pass

class Page(object):
    """
        Représente un documents textuel dans une note
    """
    def __init__(self):
        super(Page, self).__init__()
        self.text = ''

    def get_tags(self, note):
        """
            Retourne tout les tags présents dans le texte de la page sans le #
            qui prefixe le tag.

            Est un tag tout mot commencant par un dièse (#)
            suivit de N chiffres, lettres, ponctuation, caractères spéciaux
            #unTag #1autre-tag #tag.composé #premier_tag#secondtag
        """
        return set(map(lambda tag: tag[1:].strip(),
                          re.compile(r'#[^#\s]+[\s]*').findall(self.text)))



class NoteMeta(object):
    """
        Contient des informations descriptives relative à l'ensemble des
        documents que comporte une note.
        Cet objet sert à créer un objet de Note, il est sérialisé dans les
        fichiers meta.json
    """
    def __init__(self):
        super(NoteMeta, self).__init__()
        self.folder_name = ''
        self.author = None

        self.pages = list()
        self.attachments = list()

    def load_from_json(json_file):

        data = None

        with open(json_file, 'r') as f:
           data = json.load(f)

        meta = NoteMeta()

        meta.folder_name = data['folder_name']

        return meta

class SimpleNoteEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, NoteMeta):
            return self.encode_meta(obj)
        elif isinstance(obj, Note):
            return self.encode_note(obj)

        return json.JSONEncoder.default(self, obj)

    def encode_meta(self, meta):
        data = dict()
        data['folder_name'] = meta.folder_name
        if not meta.author is None:
            data['author'] = meta.author

        data['pages'] = meta.pages
        data['attachments'] = meta.attachments

        return data

    def encode_note(self, note):
        pass