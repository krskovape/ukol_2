#JSON
#dají se v něm zapisovat strukturovaná data
#nemůžu mít n-tice ; vždycky jen klíč a hodnota
#GEO JSON  = pěvně definovaná struktura; slovník něčeho a to, co to je je dáno pomocí type; můžu otevřít v GISu

import json
"""
#načítání ze stringu; pouze load načítání souboru
adict = (json.loads('{"key":12}'))
print(adict['key'])

#přidání pomocí dump - převede to z pythonu do řetězce; dumps = řetežce
adict['key2'] = None    
print(json.dumps(adict))
#dump = funguje jako reader/writer v csv
with open("output.json", "w") as f:
    json.dump(adict, f)
"""
#MODUL REQUESTS
#není základní součástí pythonu, nutná instalace (do konzole napsat: pip install requests)
#dokumentace: https://docs.python-requests.org/en/latest/ 
#stránka na errory: http.cat
#můžu z toho rovnou dostat json

import requests

URL = 'https://mapa.pid.cz/getData.php'
r = requests.get(URL)
print(r.status_code)
print(r.encoding)
#print(r.text[:100])
#print(r.json())
data = r.json()
"""
print(type(data))   #zeptám se, co jsem to dostala
print(data.keys())  #okay, slovník. Jaký máš klíče?
print(type(data['trips']))
print(data['trips'].keys())
print(data['trips']['389/2'])"""

vehicles = data['trips'].values()
#print(vehicles)

#kolik je vozidel na trati je na které lince?
lines = {}
for v in vehicles: 
    key = v['route']
    lines[key] = lines.setdefault(key,0) + 1
print(lines)


# v seznamu slovníku procházet data, uložit do slovníku a pak se ho můžu zeptat na klíč
# vehicles je seznam slovníků