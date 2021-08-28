# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count_process=input('Enter how many time processing:')
position = input('enter position of the link:')
url = input('Enter - ')

for i in range(int(count_process)):
    new_url=url
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup("a")
    patter=r"by_(\w+)"
    url=tags[int(position)-1].get('href',None)
print(re.findall(patter,url)[0])








