# no 2

import re

y = open('indonesia.txt', 'r', encoding = 'latin1')
teks = y.read()
y.close()

pola = r'di\w+'
string = re.findall(pola, teks)
print(string)
