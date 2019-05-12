import requests

def predpoved_pocasi(latitude, longitude):
	"""vrátí předpověď počasí na 5 dní po 3 hodinách pro
	zadané souřadnice"""
	url = 'http://api.openweathermap.org/data/2.5/forecast'
	parametry = {
		'lat': latitude,
		'lon': longitude,
		'appid': ___,
		'units': 'metric'
	}

	predpoved = requests.get(url, params=parametry).json()

	for prvek in predpoved['list']:
		#print(prvek)
		datum = prvek['dt_txt']
		teplota = prvek['main']['temp']
		obloha = prvek['weather'][0]['main']
		prouzek = "." * int(teplota)
		print(f'{datum} {prouzek} {teplota} {obloha}')
		


def zjisti_souradnice(misto):
	"""vrátí GPS souřadnice zadaného místa"""
	url = 'https://eu1.locationiq.com/v1/search.php'
	parametry = {
	'key': ___,
	'q': misto,
	'format': 'json'
	}
	mista = requests.get(url, params=parametry).json()
	lat = mista[0]['lat']
	lon = mista[0]['lon']
	return lat, lon

misto = input("Zadej hledané místo: ")
latitude, longitude = zjisti_souradnice(misto)
print(predpoved_pocasi(latitude, longitude))