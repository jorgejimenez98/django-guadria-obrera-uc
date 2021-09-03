def getEliminateSuccessMessage(element, elementName):
    return f'{element} ({elementName}) eliminada/o satisfactoriamente.'


def getEditedSuccessMessage(element, elementName):
    return f'{element} ({elementName}) editada/o satisfactoriamente.'


def getAddedSuccessMessage(element, elementName):
    return f'{element} ({elementName}) ingraseada/o satisfactoriamente.'


def getUniqueErrorMessage(element, elementName):
    return f'Error, ya existe un {element} con el atributo ({elementName})'


def getEliminateProtectErrorMessage(element, elementName):
    message = f'Imposible eliminar el/la {element} ({elementName}), existen otras entidades que dependen de este valor.'
    return message


def getDoubleIntegrityErrorMessage(obj, value1, obj2, value2):
    return f'Ya existe un/a {obj} de nombre {value1} en la {obj2} {value2}'


def getOfficialDistributionUpdatedSuccessMessage(workerType, day):
    return f'Distribución Oficial de {workerType} del día {day} actualizada'


def validateString(field, fieldName):
    if len(str(field).strip()) == 0:
        raise Exception('El valor {} no puede estar vacío'.format(fieldName))
    for i in str(field):
        if i in '0123456789':
            raise Exception('El valor {} no puede contener números'.format(fieldName))


def validateEmptyString(field, fieldName):
    if len(str(field).strip()) == 0:
        raise Exception('El valor {} no puede estar vacío'.format(fieldName))


def validateSelectString(field, fieldName):
    if len(str(field).strip()) == 0:
        raise Exception('Debe seleccionar obligatoriamente el valor ({})'.format(fieldName))


def getPasswordUpdatedSuccessMessage(username):
    return f'Se ha cambiado la contraseña del usuario {username} satisfactoriamente'


def getIncorrectPasswordMessage(username):
    return f'La contraseña del usuario {username} es incorrecta, inténtelo de nuevo'


def getUserRolInAString(user):
    userGroups = [i.name for i in user.groups.all()]
    if len(userGroups) == 0:
        return 'Sin Rol'
    elif len(userGroups) >= 0:
        return userGroups[0]
    return 'Error de Rol'


def getRolChangedSuccessMessage(element, username):
    return f'El rol del usuario {element} ({username}) ha sido eliminado y cambiado por el rol Estudiante-Trabajador'


def getPPAAIntegrityErrorMessage(ppaa, career, user, year):
    return f'Ya existe un {ppaa} con el usuario {user} o ya existe un PPAA del año {year} de la carrera {career}, rectifíque los datos por favor.'


def getDeanIntegrityErrorMessage(param, name, username):
    return f'Ya existe un {param} con el usuario {username} o ya existe un Decano de la Facultad {name}, rectifíque los datos por favor.'


def getHDIntegrityErrorSMS(param, name, username):
    return f'Ya existe un {param} con el usuario {username} o ya existe un jefe de Departamento del Departamento {name}, rectifíque los datos por favor.'


def getPFIntegrityErrorMessage(param, name, username):
    return f'Ya existe un {param} con el usuario {username} o ya existe un Programador de la Guardia en la Facultad {name}, rectifíque los datos por favor.'
