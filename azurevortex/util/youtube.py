import urllib.request
import re

def returnvideofromsearch(query):
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+query.replace(' ', '+'))
    id = re.findall(r'watch\?v=(\S{11})', html.read().decode())[0]

    return 'https://youtu.be/'+id