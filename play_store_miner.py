import urllib2
import json

packageName = 'com.whatsapp'      # package com.whatsapp for WhatsApp
apiKey      = '${YOUR_PLAY_STORE_API_KEY_HERE}'  # your API key
categories_file = open('categories.txt')

url = "http://api.playstoreapi.com/v1.1/apps/{0}?key={1}"
url2 = "http://api.playstoreapi.com/v1.1/top/apps/{0}?key={1}"

for category in categories_file:
    response = urllib2.urlopen(url2.format(category[:-1], apiKey))
    
    data = json.load(response)
    applist = data[category[:-1]]
    appfile = open("apps/" + category[:-1] + ".txt", "w")
    
    for l in applist:
        appfile.write(str(l)+"\n")

    appfile.close()

