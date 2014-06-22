import json
import httplib
import os

def push(value):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', "/1/classes/PlayApps" , json.dumps(value), {
           "X-Parse-Application-Id": "${YOUR_PARSE_APPLICATION_ID_HERE}",
           "X-Parse-REST-API-Key": "${YOUR_PARSE_REST_API_KEY_HERE}",
           "Content-Type": "application/json"
         })
    result = json.loads(connection.getresponse().read())
    print result

for root, dirs, files in os.walk("./details", topdown=False):
    for name in files:
        apps = open('details/' + name, 'r')
        print("\n=========== " +name[:-4] + " ============\n")
        for app in apps:
            value = eval(app[:-1])
            value['type'] = name[:-4]
            push(value)


