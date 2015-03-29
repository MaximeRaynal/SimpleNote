from django.db import models

class Tag(models.Model):
    """ Représentation d'un tag

        Les tags comportent un système de hierarchie, un parent à N enfants.
        Appliquer un tag à un élément revient à lui appliqué tout ses parents
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return '#' + self.name