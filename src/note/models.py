import os
import re

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    """ Représentation d'une note comme un ensemble de page.

        La plus part des infos sont stocké de manière physique dans les dossiers
        le stockage en BDD sert à faciliter la recherche.

        Sur le disque une note est stocké dans le dossier settings.NOTE_DIR,
        à l'intérieur d'un dossier portant le nom de l'utilisateur.
        Une note est dossier contenant les pages et les attachments.
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    privacy_state = models.CharField(max_length=20)
    creation_date = models.DateTimeField()
    last_update = models.DateTimeField()
    is_crypted = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag')

    def __init__(self):
        self.pages = list()
        return

    def __str__(self):
        return self.name

    def laod_page(self, user):
        """ Charge les pages (fichier stocké) associé à la note """
        note_directory = os.path.join(settings.NOTE_DIR, user)
        note_directory = os.path.join(note_directory, self.name)

        for element in note_directory:
            if element.endswith('.md'):
                self.pages.append(Page(element))

        return

class Page(object):
    """ Représentation d'une page

        Une page est un élément d'une note, on peut attacher des éléments à une
        page.
        Une page est stocké sur le serveur sous forme de fichier, suivant le
        principe suivant :
        Nom : ordre_NomDeLaPage
        Texte : contenu du fichier
        Tags : :see_also get_tags

    """
    def __init__(self, page_name):
        self.text = open(element, 'r').readlines()
        self.name = element.split('_')[1]
        self.order = element.split('_')[0]

    def __str__(self):
        return self.order + '_' + self.name

    def get_tags(self):
        """ Retourne tout les tags présents dans le texte de la page sans le #
            qui prefixe le tag.

            Est un tag tout mot commencant par un dièse (#)
            suivit de N chiffres, lettres, ponctuation, caractères spéciaux
            #unTag #1autre-tag #tag.composé #premier_tag#secondtag

        """
        return re.compile(r'#[^#]+[\s#]*').findall(self.text)\
                                                    .map(lambda tag: tag[1:])

class Tag(models.Model):
    """ Représentation d'un tag

        Les tags comportent un système de hierarchie, un parent à N enfants.
        Appliquer un tag à un élément revient à lui appliqué tout ses parents

    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self')

    def __str__(self):
        return '#' + self.name