from random import randint
from api.model.guard.dutyShift import DutyShift


def createRandomString(stringLength):
    letters = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    stringArray = [letters[randint(0, len(letters) - 1)] for _ in range(stringLength)]
    return ''.join(i for i in stringArray)


def createUser():
    print("Tarea Realizada OKOKOKOKOKOKOKOOKOKOK")
    DutyShift.objects.create(
        schedule='Turno {}'.format(createRandomString(10))
    )
