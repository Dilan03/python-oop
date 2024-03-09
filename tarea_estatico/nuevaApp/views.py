from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {
        'item_1': 'Escalar escalones',
        'item_2': 'Videojuegos',
        'item_3': 'Peliculas'        
                  }
    return render(request, 'nuevaApp/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el dia en que de la chamba yo me enamoré</h1>")