"""
2a) Napiš program, který se zeptá uživatele na datum 
ve formátu DD.MM.RRRR a vypíše mu na obrazovku celý 
kurzovní lístek z toho dne. Podle prvního řádku odpovědi
se můžeš přesvědčit, že jsi dostala očekávaný výstup. 
Například https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=03.05.2019
"""

import requests
datum = input("Zadej datum ve formátu DD.MM.RRRR: ")

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date='+datum

odpoved = requests.get(url)
print(odpoved.text)