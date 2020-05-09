from pypexels import PyPexels
from os import chdir
import urllib.request as req
import requests


api_key = '563492ad6f9170000100000133e1d38b49754e5ebcf024313a5fdbc2'

# instantiate PyPexels object
py_pexels = PyPexels(api_key=api_key)

for i in range(10):
    popular_photos = py_pexels.random(per_page=10)
    for photo in popular_photos.entries:
        print(photo.id, photo.photographer, photo.url)
        img_data = requests.get(photo.src['medium']).content
        with open('{0}.jpeg'.format(photo.id), 'wb') as handler:
            handler.write(img_data)
