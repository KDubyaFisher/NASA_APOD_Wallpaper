import ctypes
from fileinput import filename
import os
from urllib import response
import sys

sys.path.append('C:\Python311\Lib\site-packages')

import requests
import subprocess
import nasaapi

# Set the directory where you want to save the images 
save_directory = os.path.expanduser('~/Pictures/APOD')

# Check if the save directory exists, if not create it
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    
# Set API key to your key from nasaapi.py
yourkey = nasaapi.your_nasa_api

# Fetch the URL of the Astronomy Picture of the Day from NASA's API
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + yourkey)
response_json = response.json()
url = response_json['url']


# Download the image
filename = os.path.basename(url)
save_path = os.path.join(save_directory, filename)
response = requests.get(url)
with open(save_path, 'wb') as file:
    file.write(response.content)


# Set the downloaded image as the wallpaper
if os.name == 'posix':
    subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'file://{save_path}'])
elif os.name == 'nt':
    ctypes.windll.user32.SystemParametersInfoW(20, 0, save_path, 3)