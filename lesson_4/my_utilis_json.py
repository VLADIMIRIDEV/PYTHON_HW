import requests
import pprint
import json
import datetime as dt

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

def currency_rates(currency):
	currency = currency.upper()
	response = requests.get(URL)
	dict_json = json.loads(response.text)
	# pprint.pprint(dict_json)
	date = dt.datetime.utcnow()
	res = f"Course {currency} on {date.strftime('%d %b %Y')} is {dict_json['Valute'][currency]['Value']}"
	print(res)


if __name__ == '__main__':
	currency_rates('usd')
	currency_rates('Eur')
	currency_rates('cny')