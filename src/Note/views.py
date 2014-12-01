from django.shortcuts import render
from note.models import Note
from note.models import Tag

import json

@require_http_methods(["GET"])
def index(request):
    """ Point d'entrée de l'app appelle Angular JS """
    return HttpResponse("")

@require_http_methods(["GET"])
def notes(request):
    """ Retourne toutes les notes au format JSON """
    return HttpResponse(json.dumps(Note.objects.all()), content_type='application/json')

@require_http_methods(["GET"])
def tags(request):
    """ Retourne  tous les tags au format JSON """
    return HttpResponse("",content_type='application/json')