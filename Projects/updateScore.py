import urllib.request
import urllib.parse
import json
from time import sleep

url = 'https://api-mc360.spindance.com/api/v1/device/payment'
url2 = 'http://api.sportsdatallc.org/ncaawb-t3/games/b690a288-af7d-4379-aa03-708c9b55c30f/boxscore.json?api_key=mktedahrd8mu8swb5ucytfas'
#url3 = 'http://api.sportsdatallc.org/ncaamb-t3/games/'

values = {'machine_id' : 'SYS0007373',
          'user_acct_userid' : '12345',
          'payment_amount' : 0,
          'access_token' : '9A012D08-235B-4917-BA9E-6FF48332ED7D'}
'''
values2 = {'year' : '2015',
          'month' : '03',
          'day' : '27',
          'format': '.json'
    }
    '''
values3 = {'game_id' : "b690a288-af7d-4379-aa03-708c9b55c30f",
            'format' : '.json'
    }


Id = []
def gametostring(score):
    for x in range(len(score)):
        a = 5
       # print(Id[x][1] + " " + str(score[x][0]) + " - " + Id[x][2] + " " +  str(score[x][1]))
    #values['payment_amount'] = 250
    
def scorefn(x):
    game_master = []
    response2 = urllib.request.urlopen(url2)
    the_page2 = response2.read()
    mydict = json.loads(the_page2.decode())
    sleep(2)   
    game_master.append((mydict['home']['points'],mydict['away']['points']))
    #print("gg " , game_master)
    gametostring(game_master)
    print("hello")
    
    #return (mydict['home']['points'],mydict['away']['points'])
    print(mydict['home']['points'])
    print(mydict['away']['points'])

'''
for x in range(0,5):
    Id.append([str(mydict["games"][x]["id"]),mydict["games"][x]["home"]["name"],mydict["games"][x]["away"]["name"]])
    #Id.append(members)
    
    #if(!mydict["games"][x]["title"][0,3]
    #print(mydict["games"][x]["home"]["name"] + " vs " ,mydict["games"][x]["away"]["name"])
#values['payment_amount'] = (int(mydict["date"].split("-")[-1])//5)*25
#print(Id)
'''
sleep(2)
#print(str(scorefn(Id)) + " ")
values['payment_amount'] = scorefn(Id)[1]*25
'''
#values['payment_amount'] = scor
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()
values['machine_id'] = 'SYS0007548'
values['payment_amount'] = 250
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()
'''
