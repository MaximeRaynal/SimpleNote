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
    return HttpResponse(json.dumps(Note.objects.all()),
                                             content_type='application/json')

@require_http_methods(["GET"])
def tags(request):
    """ Retourne tous les tags au format JSON

        Le traitement (agrégation + unicité) et entièrement fait en python,
        c'est probablement plus performant qu'avec SQLite
    """
    tags_list = set()
    tags_list +=
          [note_tags for note in Note.objects.all() for note_tags in note.tags]
    return HttpResponse(json.dumps(tags_list),content_type='application/json')

@require_http_methods(["POST"])
def note_filter_by_tags(request):
    """ Retourne toutes les notes ayants les tags spécifiés """
    ##gNote.objects.filter(ta)
    return HttpResponse("",content_type='application/json')