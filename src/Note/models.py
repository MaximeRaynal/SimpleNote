from django.db import models

# Create your models here.
class Note(models.Model):
    """ Représentation d'une note comme un ensemble de page """
    name = models.CharField(max_length=50)
    description = models.TextField()
    privacy_state = models.CharField(max_length=20)
    creation_date = models.DateTimeField()
    last_update = models.DateTimeField()
    is_crypted = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    def laodPage(self):
        """ Charge les pages (fichier stocké) associé à la note """
        return ''


class Tag(models.Model):
    """ Représentation d'un tag """
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self')

    def __str__(self):
        return '#' + self.name