# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input('Count: '))
position = int(input('Position: '))-1
url =  input('Enter - ')
ls=list()
html = urllib.request.urlopen(url, context=ctx).read()
for i in range(count):
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   for tag in tags:
     ls.append(tag.get('href',None))

   link=ls[position]
   print(link)
   html=urllib.request.urlopen(link, context=ctx).read()
   ls.clear()
