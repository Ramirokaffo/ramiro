
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
import os

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
def test(request):
    return render(request, 'test.html', context = {})



@csrf_exempt
def pwd(request: WSGIRequest):
    if request.method == 'POST':
        mon_fichier = request.FILES.get('file')
        if mon_fichier:
            nom_fichier = mon_fichier.name
            chemin_fichier = os.path.join('media/', nom_fichier)

            with open(chemin_fichier, 'wb') as destination:
                for morceau in mon_fichier.chunks():
                    destination.write(morceau)
    # context = {
    #     "title": "À propos de nous"
    # }
    # return render(request=request, template_name="about.html", context=context)
