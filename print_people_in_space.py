# How many humans are in space right now ...The answer is below :)
# link : http://open-notify.org/Open-Notify-API/People-In-Space/

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

number = json.get("number")

print ('\nHow many people are in space right now?')
print('There are currently', number, 'people in space right now.')

print('\nThe name of the people currently in space are:\n ')
for person in json['people']:
    print(person['name'])
