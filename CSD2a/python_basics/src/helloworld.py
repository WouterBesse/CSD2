print ('Vul uw naam in a.u.b.')
naam = input()
dagdeel = 'appel'

import datetime
tijd = datetime.datetime.now();
if tijd.hour <= 4:
    dagdeel = 'nacht'
elif tijd.hour > 4 and tijd.hour <= 12:
    dagdeel = 'morgen'
elif tijd.hour > 12 and tijd.hour <= 18:
    dagdeel = 'middag'
elif tijd.hour > 18 and tijd.hour <= 23:
    dagdeel = 'avond'
else:
    dagdeel = 'nacht'


print('Goede', dagdeel, naam, ', vandaag zijn de rozen rood en is de lucht blauw. Indien dit niet het geval is wordt door experts aangeraden dit script op een andere dag uti te voeren.')
