def can_invest (plec, wiek, poziomzdolnosci):
    if wiek<18 or poziomzdolnosci<50:
        return print ("nie mozesz inwestowac")
    if wiek>18 and poziomzdolnosci >60:
        return print("zainwestuj w zloto")
    elif wiek>18 and poziomzdolnosci>70:
        return print ("zainwestuj w papiery wartosciowe")
    elif wiek > 18 and poziomzdolnosci > 80:
        return print("zainwestuj na giełdzie")
    elif wiek > 18 and poziomzdolnosci > 50:
        return print("kup dom")
