import random
import datetime

def options(day):
    restaurants = ['japochungo','covas','japo4','pimpa','girasuelos','suamu','cuoco','trobada','nurivan','milcasas','quaranta','fantastic','motobar']
    if day == 4:
        return 'chipo'
    elif day == 0 or day == 3:
        return restaurants[1:]
    else:
        return restaurants

today = datetime.datetime.today().weekday()

restaurants_chosen = []

loop = True

options_today = options(today)

print 'Type DONE to select restaurant'
print "Today's options are: %s" % options_today
while loop:
    option = raw_input('Insert Option:')
    if option in options_today:
        restaurants_chosen.append(option)
    elif option == 'DONE':
        loop = False
    else:
        print 'Insert a valid option or DONE to finish'

print 'From this list %s the winner is....' % restaurants_chosen
print random.choice(restaurants_chosen)