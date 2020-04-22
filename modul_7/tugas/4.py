# nomer 4

import re

f = open('KEI.html', 'r', encoding = 'latin1')
teks = f.read()
f.close()

pola = r'(\w+)</a></td>'
string = re.findall(pola, teks)
print(string)

g = open('KEI.html', 'r', encoding = 'latin1')
teks2 = g.read()
g.close()

pola2 = r'(\w+)</a></td>\n<td>(\d.\d+)'
tuples = re.findall(pola2, teks2)
print (" --- mengeluarkan angka ---")
print(tuples)

print(" --- list of tuples --- ")
tupp = [(t[0], float(t[1]))for t in tuples]
print(tupp)
