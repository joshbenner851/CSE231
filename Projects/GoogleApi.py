#googlemaps
from googlemaps import Client
import urllib3, urllib
import json
#a = "https://maps.googleapis.com/maps/api/geocode/json?address=new york, new york"
location = "Grand Rapids,MI"

#print(a)
def formatString(location):
    location = location.split(",")
    location = location[0].split(" ")
    name =""
    for x in location:
        name += x + " "
    name = name[:-1]
    print(name)
    location.append(name)
    print(location)
'''
name = ""
for x in location:
    name += x + "+"
print(name)
for x in name:
    name = x + "+"
places += "%7C"'''
def saveImage(img):
    f=open("stuff"+".jpg","wb")
    f.write(img.read())
    f.close()
url = "https://maps.googleapis.com/maps/api/staticmap?size=1000x1000&maptype=roadmap\&markers=size:mid%7Ccolor:red%7C" + "Grand+Rapids" + "%7C"
req = urllib.request.Request(url, None,headers={'User-Agent' : 'Mozilla/5.0'})
img = urllib.request.urlopen(req)
#str_response = img.readall().decode('utf-8')
saveImage(img)


'''

c = Client(key="AIzaSyD8FeWwYigz2Tm7if6daEJkftxb2Hc2QS8")

d = c.directions("texarkana","atlanta")
steps = c.directions("texarkana","atlanta")[0]["legs"][0]["steps"]

for d in steps:
    print(d['html_instructions'])

'''
