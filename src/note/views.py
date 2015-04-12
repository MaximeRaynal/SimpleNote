from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from note.models.note import Note
from note.models.tag import Tag

import json

@require_http_methods(["GET"])
@login_required
def index(request):
    """ Point d'entrée de sert l'application HTML JS CSS """
    return render(request, 'note/index.html')

@require_http_methods(["GET"])
@login_required
def notes(request):
    """ Retourne toutes les notes au format JSON """
    return HttpResponse(json.dumps(
                    list(Note.objects.filter(author=request.user).values())),
                        content_type='application/json')

@require_http_methods(["GET"])
@login_required
def note_by_id(request, note_id):
    """ Retourne la note ayant l'id passé en paramètre """
    note = get_object_or_404(Note, pk=note_id)
    return HttpResponse(json.dumps(note.__dict__),
                        content_type='application/json')

@require_http_methods(["GET"])
@login_required
def tags(request):
    """ Retourne tous les tags au format JSON

        Le traitement (agrégation + unicité) et entièrement fait en python,
        c'est probablement plus performant qu'avec SQLite
    """
    tags_list = set()
    tags_list = [note_tags for note in Note.objects.filter(author=request.user)
                           for note_tags in note.tags]
    return HttpResponse(json.dumps(tags_list),content_type='application/json')

@require_http_methods(["POST"])
@login_required
def notes_filter_by_tags(request):
    """ Retourne toutes les notes ayants les tags spécifiés """
    tags_list = json.load(request.POST['tags_list'])
    note_list = Note.objects.filter(tags__name__in=tags_list).values()
    return HttpResponse("",content_type='application/json')


@require_http_methods(["POST"])
@login_required
def save_note(request):
    """ Fonction de serialization / sauvegarde d'une note

        Cette fonction est appellé automatiquement, régulière par la WebApp
        Elle doit :
            - Regarder si la note existe déjà, sinon la créer
            - Sauvegarder les modifications dans les fichiers correspondants
            - Mettre à jour la base de donnée pour faciliter les recherches
            - Renvoyer un code HTTP correspondant
    """
    pass


