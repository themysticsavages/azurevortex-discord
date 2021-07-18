import requests
import json

def getdog():
    r = json.loads(requests.get('https://dog.ceo/api/breeds/image/random').text)['message']
    return r