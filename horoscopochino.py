"""
HOROSCOPO CHINO
"""

# LOGICA DIAGRAMA DE FLUJO


# LOGICA EN TERMINAL


# MOCKUP EN WEB MOCKUP FLASK

import os
import sys

HOROSCOPO = {
    1: "Rata",
    2: "Buey",
    3: "Tigre",
    4: "Conejo",
    5: "Dragon",
    6: "Serpiente",
    7: "Caballo",
    8: "Cabra",
    9: "Mono",
    10: "Gallo",
    11: "Perro",
    12: "Cerdo"

}


def run():


    try:
        completado = False

        while completado == False:
            ano = int(input("Introduce el año que naciste: "))
            anoInit = 1912
            if (ano <= 0):
                pass
            else:
                count = 1
                # mejor usar el ano % len(HOROSCOPO)
                for i in range(1900, ano):
                    if ano == i:
                        # completado = True
                        break;

                    count += 1
                    if count > 12:
                        count = 1



                if count in HOROSCOPO:
                    print("ERES DEL HOROSCOPO " + HOROSCOPO[count])
                else:
                    print("no ta en horoscopo")
                    raise ValueError

    except ValueError:
        print("ERrror VALOR")
        run()


# punot inicial
if __name__ == '__main__':
    os.system("cls")
    run()
