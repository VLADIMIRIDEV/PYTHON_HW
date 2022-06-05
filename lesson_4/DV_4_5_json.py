import my_utilis_json

if __name__ == "__main__":

	import sys

	currency_list = sys.argv[1:]
	for currency in currency_list:
		currency = my_utilis_json.currency_rates(currency)
		print(str(currency))

	# currency = tuple(map(my_utilis.currency_rates, currency_list))
	# print(currency)
