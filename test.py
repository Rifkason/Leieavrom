from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "RH_db"

#Funksjonen "get_collection" denne funksjonen kobler til MongoDB-database og henter samlingen som er angitt. som er valigvis ("leiere")
def get_collection(col):
    cluster = MC(CONNECTION_STRING)
    database = cluster[DATABASE]
    collection = database[col]
    return collection

#"lagre_objekt" denne funksjonen ber våre brukere om å legge inn informasjon som "navn, telefonnummere og epost"
#den lagrer denne informasjonen/dataene i MongoDB-databasen.
def lagre_objekt(indata="leiere"):
    navn = input("legg til ditt navn: ")
    Tlf = input("Tlf: ")
    Epost = input("Epost: ")
    nyeleier = {"navn": navn, "Tlf": Tlf, "Epost": Epost}
    get_collection(indata).insert_one(nyeleier)


# "slett_objekt" denne funksjonen lar brukeren slette leiers informasjon ved å oppgi navnet. 
# Den tar leierne it av MongoDB-database.

# framtids plan: denne funksjonen bruker vi til å slette leiere som enten har sluttet eller ikke burde ha tilgang lenger.
#tanken er at etter vært så skal leiern få tilabke meldign på hvorfor de er slettet/tatt bort)
def slett_objekt(indata="leiere"):
    col = get_collection(indata)
    navn = input("Skriv in navnet på personen du ønsker og slette: ")

    col.delete_one({"navn": navn})

    print(f"vi har sletten leieren med navn: {navn}")

#"print_mappe" denne funksjonen skriver ut data om rom, spesielt de som er merkert som ledig.
#den bruker "indata" for å hente informasjon fra MongoDB-samlinger.
def print_mappe(inndata):
    col = get_collection(inndata).find()
    listeOfdata = []
    #denne henter rom som er skrevet som ledig, slik at leierne kan finne ut hva slags rom de kan leie og ikke.
    for c in col:
        if c["er rommet ledig?"] == "ledig":
            print(f"{c['rom']} {c['er rommet ledig?']}")

        listeOfdata.append(c)
    return listeOfdata

#"rom_ledigikke" =indata, brukeren kan leie and frigi et rom med denne funksjonen.
#den oppdaterer et bestemt rom i MongoDB-database status.

# framtids plan: dette er her leierne kan leie rom eller si up rom, tanken er å få det slikt at man kan søk om rommet på et Kl slet.
#istede får å ta rommet hele tiden.
#slikt at det holder seg rolig og at man ungår kras mellom leierne.
def rom_ledigikke(indata="rom"):
    col = get_collection(indata)
    romnavn = input("skriv in rommet du ønsker og leie: ")
    ønsker = input("vil du ha rommet skriv ja: ")
    ledig = ""
#denne forandrer ledig = ikke ledig. vis leieren skriver ja, vis nei så blir coden den samme og holder seg ledig.
    if ønsker == "ja":
        ledig = "ikke ledig"

    if ønsker == "nei":
        ledig = "ledig"

    filter = {"rom": romnavn}
    updatering = {'$set': {'rom': romnavn, 'er rommet ledig?': ledig}}
    col.update_one(filter, updatering)

#"menu_menu" denne hovedmenyen gir brukerne en rekke alternativer, som å legge til, leie eller frigi.
#se på romstatus eller avslutt programmet.
def menu_menu():
    while True:
        print("Velkommen til mitt fengsel bygg: ")
        print("1. får og legge til en leier: ")
        print("2. får og slette en leier: ")
        print("4. får og leie et rom: ")
        print("6. print ut rom: ")
        print("0. får og avslutt: ")
        valg = input("velg et nummer fra listen over: ")

        #disse tallene skriver leiern in får å komme til den og den funksjonen i koden, tanken er at leiern skal kun får 4 valg.
        #enten lag bruker, leie av rom, se hva slags rom er ledig, lagring av bruker eller å gå ut av menu.
        if valg == "1":
            lagre_objekt()
        
        elif valg == "2":
            slett_objekt()

        elif valg == "4":
            rom_ledigikke()

        elif valg == "6":
            print_mappe("rom")

        elif valg == "0":
            print("Goodbye :)")
            break

menu_menu()