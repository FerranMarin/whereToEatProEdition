import re
import json
import datetime
import time
import random
from slackclient import SlackClient

def options(day):
    restaurants = ['japochungo','covas','japo4','pimpa','girasuelos','suamu','cuoco','trobada','nurivan','milcasas','quaranta','fantastic','motobar']
    if day == 4:
        return 'chipo'
    elif day == 0 or day == 3:
        return restaurants[1:]
    else:
        return restaurants

token = "xxx-token-xxx"
sc = SlackClient(token)

today = datetime.datetime.today().weekday()
options_today = options(today)

if sc.rtm_connect():
    while True:
        x = sc.rtm_read()
        if len(x) > 0 and 'text' in x[0].keys():
            if 'user' not in x[0].keys(): continue
            name = sc.api_call("users.info",user=x[0]['user'])
            rname = json.loads(name)
            #print x[0]
            print rname['user']['name'],[rname['user']['id']],'channel',[x[0]['channel']],x[0]['text']
            if x[0]['text'] == 'help':
                sc.rtm_send_message(x[0]['channel'], "activate me using '!eat start' without commas")
                sc.rtm_send_message(x[0]['channel'], "check chosen restaurants so far '!eat check' without commas")
            if re.match(r'!eat',x[0]['text']) != None:
                paction = str(x[0]['text'])
                action = paction.lstrip('!eat ')
                if action == 'start':
                    sc.rtm_send_message(x[0]['channel'], "Starting #WheretoEatProEdition")
                    restaurants_chosen = []
                    msg = "Today's options are: %s" % options_today
                    sc.rtm_send_message(x[0]['channel'],msg)
                    sc.rtm_send_message(x[0]['channel'],"Type !eat <option> to add restaurant to today's pool")
                elif action in options_today:
                    restaurants_chosen.append(action)
                    msg = "Restaurant '%s' added" % action
                    sc.rtm_send_message(x[0]['channel'], msg)
                elif action == 'check':
                    msg = "Restaurants in today's pool are:%s" % restaurants_chosen
                    sc.rtm_send_message(x[0]['channel'], msg)
                elif action == 'finish':
                    msg = "From this list %s the winner is...." % restaurants_chosen
                    sc.rtm_send_message(x[0]['channel'], msg)
                    winner = random.choice(restaurants_chosen)
                    sc.rtm_send_message(x[0]['channel'], winner)
                    restaurants_chosen = []
                else:
                    sc.rtm_send_message(x[0]['channel'], "Incorrect Command")
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
