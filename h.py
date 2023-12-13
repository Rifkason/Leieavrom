from datetime import datetime, timedelta

def rom_ledigikke(indata="rom"):
    col = get_collection(indata)
    romnavn = input("Skriv inn rommet du ønsker å leie: ")


    rom = col.find_one({"romnavn": romnavn})

    if rom:

        if sjekk_ledighet(rom):
            print(f"Rommet {romnavn} er ledig!")

        else:
            print(f"Rommet {romnavn} er ikke ledig.")

    else:
        print(f"Rommet {romnavn} eksisterer ikke i systemet.")

def sjekk_ledighet(rom):

    ledig_til = rom.get("ledig_til")

    if ledig_til:
        ledig_til_dato = datetime.strptime(ledig_til, "%Y-%m-%d")
        nåværende_dato = datetime.now()


        if nåværende_dato < ledig_til_dato:
            return True
        else:
            return False
    else:

        return False
    
def menu_menu():
    while True:
        print("Velkommen til mitt fengsel: ")
        print("1. får og leie et rom: ")

        print("0. får og piss off: ")
        valg = input("velg et nummer fra listen over: ")
        if valg == "1":
            rom_ledigikke()

        elif valg == "0":
            print("Will you kindly piss off my good sir, have a nightmare filled night :)")
            break

menu_menu()