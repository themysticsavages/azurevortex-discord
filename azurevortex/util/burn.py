import imgkit
import base64
import json
import random
import requests
import os

imgurimg = 'justsomeimagefromazurevortex{}.png'.format(random.randrange(1, 100000))
os.chdir(os.getcwd())


def burn(text):
    with open('index.html', 'w') as f:
        f.write('<div id="fire">'+text+'</div> <style> body { background-color:#222; text-align:center; font-family: "Open Sans"; } #fire { color: #f5f5f5; text-shadow: 0px -2px 4px #fff, 0px -2px 10px #FF3, 0px -10px 20px #F90, 0px -20px 40px #C33; font-size: 100px; } </style>')
    f.close()
    imgkit.from_file('index.html', 'img.png')
    os.remove('index.html')
    u = requests.post('https://api.imgur.com/3/upload.json', headers = {"Authorization": "Client-ID {}".format(json.loads(open('./config.json', 'r').read())['imgurid'])},
    data = {
        'key': json.loads(open('./config.json', 'r').read())['imgursecret'], 
        'image': base64.b64encode(open('./img.png', 'rb').read()),
        'type': 'base64',
        'name': imgurimg,
        'title': 'Burning!'
    })
    data = json.loads(u.text)['data']
    os.remove('img.png')
    return data['link']