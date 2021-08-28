import re

words="  hi bro lal eka inna oni mona wunath 64647 HI"
word="mefsdf@com54364"
lal=words.strip()
print(words.strip())

print(re.findall('[0-9]+',words))
print(re.findall('[A-Z]+',words))
print(re.findall('\w+',words))
print(re.findall('^m+\w+@$',word))
print(re.findall('([a-z]+)([0-9]+)',word))
print(re.findall('(h{1,4})+',words))
print(re.split('@',word))
print(re.sub('(\d+)+','num',words))
print(re.search('hi',words))




