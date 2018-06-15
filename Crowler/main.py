
from suds.client import Client
import time

import unidecode

# Definiuje plik wejsciowz
url = 'https://webapi.allegro.pl/service.php?wsdl'
client = Client(url)

# Wpisz swoje webapi
webAPI = '74322389'
countryId = 1

filtr_query = client.factory.create('ArrayOfFilteroptionstype')


tablica = { 'category': '67524',
            #'category': '253062', miliataria
           #'condition': 'used',
           'search': ''
           }
rangeUp = len(tablica) - 1

for i in range(0, rangeUp):
    filtr = client.factory.create('FilterOptionsType')
    filtr.filterId = tablica.keys()[i]
    filtrAOS = client.factory.create('ArrayOfString')
    filtrAOS.item = tablica.values()[i]
    filtr.filterValueId = filtrAOS
    filtr_query.item.append(filtr)

wynik = client.service.doGetItemsList(webAPI, countryId, filtr_query, resultScope=3, resultSize=1000)
print "Otrzymano %d wynikow." % wynik.itemsCount, "Sukces! %s " % time.strftime("%A, %H:%M:%S")

print wynik.itemsList[0][0].itemTitle
list = wynik.itemsList[0]

wyjscie = open("agd.txt", "w")

for x in list:
    w = x.itemTitle
    z=unidecode.unidecode(w)
    z=z+"\n"
    wyjscie.write(z.lower())



