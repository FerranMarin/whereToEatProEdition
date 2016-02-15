import datetime
import random

restaurants = ['japochungo','covas','japo4','pimpa','girasuelos','suamu','cuoco','trobada']

hoy = datetime.datetime.today().weekday()

def choose(x):
    if x == 4:
        return 'chipo'
    elif x == 0:
        return random.choice(restaurants[1:])
    else:
        return random.choice(restaurants)

print choose(hoy)