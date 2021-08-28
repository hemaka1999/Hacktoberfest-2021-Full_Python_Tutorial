import re
text="chuti patiya nidi hhttthtgdg httss cfgi"
print(re.search('(^c.+i$)?',text))
print(re.search('[^zx]',text))
print(re.search('\bch',text))

