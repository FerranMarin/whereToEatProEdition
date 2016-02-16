import datetime
import random

def choose(x):
    if x == 4:
        return 'chipo'
    elif x == 0 or x == 3:
        return random.choice(restaurants[1:])
    else:
        return random.choice(restaurants)





restaurants = ['japochungo','covas','japo4','pimpa','girasuelos','suamu','cuoco','trobada']

hoy = datetime.datetime.today().weekday()

print choose(hoy)