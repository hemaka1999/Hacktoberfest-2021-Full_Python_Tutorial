import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urlopen(url, context=ctx).read().decode()
print(data)
counts=0
info = json.loads(data)
print('User count:', len(info['comments']))
for i in range(len(info['comments'])):
    counts=counts+info["comments"][i]["count"]
print(counts)




