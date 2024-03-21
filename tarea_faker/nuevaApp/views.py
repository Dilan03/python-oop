from django.shortcuts import render
from nuevaApp.models import Toyota_Legacy
#from django.http import HttpResponse

# Create your views here.
def index(request):
    people_lists = Toyota_Legacy.objects.all()
    my_context = {
        'item_1': 'Escalar escalones',
        'item_2': 'Videojuegos',
        'item_3': 'Peliculas', 
        'people_list': people_lists     
    }
    
    return render(request, 'nuevaApp/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el dia en que de la chamba yo me enamoré</h1>")