""" Programma dat de locaties op kan zoeken van betreffende latitudes en longitudes. Deze coördinaten worden van een CSV ingelezen
    waarna de straatnaam wordt geselecteerd uit het JSON format. Deze worden toegoegd aan een lijst en daarna geëxporteerd als een nieuw
    CSV bestand naar de Desktop. || Creator: Lars van der Water, 2020"""

import requests
import csv
from pandas import DataFrame

# open csv bestand met de coordinaten van de klant
f = open("voorbeeld.csv")
reader = csv.reader(f)

# maak een lege adressen lijst
adressen = []

# loop door elke combinatie latitudes en longitudes in het csv bestand
for latitude, longitude in reader:

    # vraag de locatie op via de tomtom API
    response = requests.get("https://api.tomtom.com/search/2/reverseGeocode/{}%2C{}.json?returnRoadUse=true&key=uISDs7QR4Ru4o6Cn1xavVvggapKvcxhG".format(latitude, longitude))

    # zet de informatie van de betreffende coördinaten om in een JSON format
    data = response.json()
    
    # selecteer alleen het adres van de coördinaten
    tussendata = data.get('addresses')
    alle_data = tussendata[0]
    adres = alle_data.get('address', {}).get('freeformAddress')
    
    # voeg adres toe aan lijst
    adressen.append(adres)

# zet lijst om naar pandas dataframe
df = DataFrame(adressen, columns=['locaties'])

# exporteer als export_dataframe.csv naar de desktop van ...
export_csv = df.to_csv (r'C:\Users\Larry\Desktop\export_dataframe.csv', index=None, header=True)