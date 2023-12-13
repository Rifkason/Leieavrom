from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "RH_db"

def get_collection(col):
    cluster = MC(CONNECTION_STRING)
    database = cluster[DATABASE]
    collection = database[col]
    return collection

def rom_ledigikke(indata="rom"):
    col = get_collection(indata)
    romnavn = input("skriv in rommet du ønsker og leie: ")
    ønsker = input("vil du ha rommet skriv ja: ")
    ledig = ""
    if ønsker == "ja":
        ledig = "ikke ledig"
    if ønsker == "nei":
        ledig = "ledig"
    #nyttromnavn = input("vis du vill ha rommet skriv nei: ")
    #nyromnavn = {"romnavn": romnavn, "ønsker": ønsker}
    filter = {"rom": romnavn}
    updatering = {'$set': {'rom': romnavn, 'ledig': ledig}}
    col.update_one(filter, updatering)

rom_ledigikke()
