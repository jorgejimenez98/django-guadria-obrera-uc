from django.contrib.auth.decorators import user_passes_test


def checkUserAccess(rol, login_url=None):
    """
    Decorador para comprobar que un usuario tiene un rol dado, de no tenerlo lanza la vista ala url que se pasa por
    parametro, se utizila la funcion user_passes_test de django.contrib.auth.decorators.
    """

    def userHasRol(user):
        if user.groups.filter(name='Superusuario').exists():
            return True
        elif user.groups.filter(name=rol).exists():
            return True
        return False

    return user_passes_test(userHasRol, login_url=login_url)
