def getGuardByUniversitySeatName(universitySeatName, guardList):
    for guard in guardList.all():
        if guard.universitySeat.name == universitySeatName:
            return guard
    return None
