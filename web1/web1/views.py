from django.http import HttpResponse

def saludo(request): # Nuestra primera vista

    documento = """<html>
    <body>
    <h1>
    Hola profe, esta es nuestra primera vista usando el MVC, en python django se llama Model Template View.
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)