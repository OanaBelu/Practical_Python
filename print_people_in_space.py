# How many humans are in space right now ...The answer is below :)
# link : http://open-notify.org/Open-Notify-API/People-In-Space/

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people currently in space are: ')
for person in json['people']:
    print(person['name'])