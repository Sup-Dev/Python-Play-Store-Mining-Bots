import urllib2
import json

file_name = "game_widgets"
packages = open("apps/" + file_name + ".txt", 'r')
apiKey = '${YOUR_42MATTERS_API_KEY}'
app_details = open("details/" + file_name + ".txt", "w")

for app in packages:
    packageName = app[:-1]
    print(packageName)
    url = "https://42matters.com/api/1/apps/lookup.json?p={0}&access_token={1}"
    response = urllib2.urlopen(url.format(packageName, apiKey))
    data = json.load(response)

    content = {}

    content['package_name'] = data['package_name']
    content['category'] = data['category']
    content['content_rating'] = data['content_rating']

    if(data.has_key('downloads')):
        content['downloads'] = data['downloads']
    else:
        content['downloads'] = ''
        
    content['market_update'] = data['market_update']
    content['promo_video'] = data['promo_video']
    content['rating'] = data['rating']

    if(data.has_key('size')):   
        content['size'] = data['size']
    else:
        content['size'] = 0
        
    content['screenshots'] = data['screenshots']
    content['title'] = data['title']
    content['version'] = data['version']
    content['developer'] = data['developer']
    content['number_ratings'] = data['number_ratings']
    content['price'] = data['price']
    content['icon'] = data['icon']
    content['icon_72'] = data['icon_72']
    content['market_url'] = data['market_url']
        
    app_details.write(str(content)+"\n")
#print(data)

app_details.close()
packages.close()









"""

import urllib2
import json

file_name = 'com.amazon.kindle'
apiKey = '4ce91674966ce650a354ebd18b450615334e4a59'
app_details = open("details/" + "books_and_reference" + ".txt", "a")
url = "https://42matters.com/api/1/apps/lookup.json?p={0}&access_token={1}"

response = urllib2.urlopen(url.format(file_name, apiKey))

data = json.load(response)

content = {}

content['package_name'] = data['package_name']
content['category'] = data['category']
content['content_rating'] = data['content_rating']
content['downloads'] = data['downloads']
content['market_update'] = data['market_update']
content['promo_video'] = data['promo_video']
content['rating'] = data['rating']
content['size'] = data['size']
content['screenshots'] = data['screenshots']
content['title'] = data['title']
content['version'] = data['version']
content['developer'] = data['developer']
content['number_ratings'] = data['number_ratings']
content['price'] = data['price']
content['icon'] = data['icon']
content['icon_72'] = data['icon_72']
content['market_url'] = data['market_url']

app_details.write(str(content)+"\n")
app_details.close()
print(content)

"""
