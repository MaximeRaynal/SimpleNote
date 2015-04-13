from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@require_http_methods(["GET"])
@login_required
def index(request):
    """ Point d'entrée de sert l'application HTML JS CSS """
    return render(request, 'webapp/index.html')