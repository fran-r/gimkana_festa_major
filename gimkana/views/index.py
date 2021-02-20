from django.shortcuts import render

from ..models import Qr, UserTest


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_qrs = Qr.objects.all().count()
    num_users = UserTest.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
            'num_qrs': num_qrs,
            'num_users': num_users,
            'num_visits': num_visits,
        },
    )
