from django.shortcuts import render
from django.http  import HttpResponseNotFound

def index(request):
    return render (request, "index.html")

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1> Pagina no encontrada </h1>')

def About(request):
    return render(request, 'acerca de nosotros.html')


