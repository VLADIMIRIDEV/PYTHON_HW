from datetime import datetime as dt

from requests import get


def currency_rates(currency):
	url = 'http://www.cbr.ru/scripts/XML_daily.asp'
	currency = currency.upper()
	response = get(url)
	if response:
		currency_split = response.text.split(currency)
		value_split = currency_split[1].split('</Value>')[0].split('<Value>')[1]
		value = float(value_split.replace(',', '.'))
		date_time = dt.now()
		date = date_time.strftime("%d.%m.%Y")

		return (f'{currency} {value} on {date}')

	else:
		return None


if __name__ == '__main__':
	print(currency_rates('usd'))
	print(currency_rates('Eur'))
	print(currency_rates('cny'))