from django.http import HttpResponse

def saludo(request): # Nuestra primera vista

    return HttpResponse("Hola profe, esta es nuestra primera vista usando el MVC, en python django se llama Model Template View")