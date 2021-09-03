from datetime import date

today = date.today()


def getTodayDayOnAString():
    todayDay = f'0{today.day}' if today.day <= 9 else today.day
    todayMonth = f'0{today.month}' if today.month <= 9 else today.month
    return '{}-{}-{}'.format(today.year, todayMonth, todayDay)


def getTodayDayOnACompleteString():
    monthsString = 'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre'
    weekDays = 'Lunes Martes Miércoles Jueves Viernes Sábado Domingo'
    months = {i[0] + 1: i[1] for i in enumerate([e for e in monthsString.split()])}
    weekDict = {i[0]: i[1] for i in enumerate([e for e in weekDays.split()])}
    return f'{weekDict[today.weekday()]} {today.day} de {months[today.month]} del {today.year}'
