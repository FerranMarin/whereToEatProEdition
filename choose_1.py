import random

restaurants = []
loop = True

print 'Type DONE to select restaurant'
while loop:
    option = raw_input('Insert Option:')
    if option == 'DONE' or '':
        loop = False
    else:
        restaurants.append(option)

print 'From this list %s the winner is....' % restaurants
print random.choice(restaurants)