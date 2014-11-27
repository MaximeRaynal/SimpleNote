from django.shortcuts import render
from Note.models import Note
from Note.models import Tag

import json


def index(request):
    """ Point d'entrée de l'app appelle Angular JS """
    return HttpResponse("")

def notes(request):
    """ Retourne toutes les notes au format JSON """
    return HttpResponse(json.dumps(Note.objects.all()), content_type='application/json')

def tags(request):
    """ Retourne  tous les tags au format JSON """
    return HttpResponse("",content_type='application/json')