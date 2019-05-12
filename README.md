# ukoly-ke-knihovne-requests

Zadání:

1a. Napiš funkci `zjisti_souradnice(misto)`, která vráti dvojici GPS souřadnic desetinných čísel `(lat, lon)` (takže například `(49.1922443, 16.6113382)`). Převodu názvu místa na GPS souřadnice se "geocoding". Můžeš k tomu využít např. služby LocationIQ, https://locationiq.com/docs-html/index.html#forward_usage Použijte první výsledek ze seznamu odpovědi poskytnuté API.

1b. Uprav program pro získání předpovědi počasí z libovolného místa na světě (např. z Mt. Everest), který jsme dělali na srazu, tak, aby se uživatele zeptal na název místa a následně vypsal předpověď pro toto místo. Využij k tomu funkci `zjisti_souradnice` z předchozího úkolu. Využij k tomu variantu API, která konzumuje GPS souřadnice (https://openweathermap.org/forecast5#geo5)

2a. Napiš program, který se zeptá uživatele na datum ve formátu DD.MM.RRRR a vypíše mu na obrazovku celý kurzovní lístek z toho dne. Podle prvního řádku odpovědi se můžeš přesvědčit, že jsi dostala očekávaný výstup. Například https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=03.05.2019

2b. Napiš program, který se uživatele zeptá na množství na kód měny (`HRK`), stáhne aktuální směnný kurz ČNB (https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt) a vypíše hodnotu kurzu.
