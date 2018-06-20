
from suds.client import Client
import time

import unidecode

url = 'https://webapi.allegro.pl/service.php?wsdl'
client = Client(url)




webAPI = '74322389'
countryId = 1

filtr_query = client.factory.create('ArrayOfFilteroptionstype')


tablica = { 'category': '257933', #lustrz
            #'category': '253062', miliataria
            # 486 komputery stacjonarne
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


i=0
for x in list:
    out= open("lustrz"+str(i), "w")
    w = x.itemTitle
    z=unidecode.unidecode(w)
    z=z+"\n"
    out.write(z.lower())
    out.close()
    i=i+1
    if(i==1000):
        break




