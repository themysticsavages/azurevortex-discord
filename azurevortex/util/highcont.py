import os
from PIL import Image, ImageEnhance, UnidentifiedImageError
import base64
import json
import random
import requests

imgurimg = 'justsomeimagefromazurevortex{}.png'.format(random.randrange(1, 100000))
os.chdir(os.getcwd())
os.chdir('util')

def highcont(img):
    img_data = requests.get(img).content
    with open('img.png', 'wb') as handler:
        handler.write(img_data)
    handler.close()
    
    try:
        im = Image.open('./img.png')
        enhance = ImageEnhance.Contrast(im)
    except UnidentifiedImageError:
        os.remove('./img.png')
        return 'You did not supply a proper image URL!'

    im_output = enhance.enhance(5)
    im_output.save('img.png')

    u = requests.post('https://api.imgur.com/3/upload.json', headers = {"Authorization": "Client-ID {}".format(json.loads(open('./config.json', 'r').read())['imgurid'])},
    data = {
        'key': json.loads(open('./config.json', 'r').read())['imgursecret'], 
        'image': base64.b64encode(open('./img.png', 'rb').read()),
        'type': 'base64',
        'name': imgurimg,
        'title': 'High contrast!'
    })
    data = json.loads(u.text)['data']
    os.remove('./img.png')
    return data['link']