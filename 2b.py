"""
2b. Napiš program, který se uživatele zeptá na množství na kód měny (`HRK`), 
stáhne aktuální směnný kurz ČNB 
(https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt) 
a vypíše hodnotu kurzu. Pro rozsekání textu na řádky použij metodu `textova_odpoved.splitlines()`, 
pro rozsekání řádku na seznam (list) částí oddělených `|` udělá `radek.split('|')`
"""

import requests

mena = input('Zadej kód měny: ')

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt'
odpoved = requests.get(url).text

radky = odpoved.splitlines()

for radek in radky:
	if mena in radek:
		seznam = radek.split('|')
		print(f'Aktuální kurz pro měnu {mena} ({seznam[1]}) je {seznam[-1]}')

