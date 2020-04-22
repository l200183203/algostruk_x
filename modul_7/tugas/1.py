# no 1

import re

x = open('indonesia.txt', 'r', encoding = 'latin1')
teks = x.read()
x.close()

pola = r'\sme\w+'
string = re.findall(pola, teks)
print(string)
