# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

VALID_EMAIL = re.compile(r'(?P<username>[a-zA-Z0-9]+[_.-]*[a-zA-Z0-9]+)@(?P<domain>[a-z]+\.[a-z]{2,})')
# VALID_EMAIL = re.compile(r'^\w*@\w*\.(com|ru)$')


def email_parse(address):
	result = {}

	try:
		if VALID_EMAIL.match(address):
			for arg in address:
				login, domain = re.split(r'@', address)
				result['login'] = login
				result['domain'] = domain
		else:
			raise ValueError
	except ValueError:
		return print(f'ValueError: wrong email: {arg}')
	return result


if __name__ == '__main__':
	test_emails = ['allisposible@mail.ru', 'someone@geekbrainsru', 'cumba@bk.ru', 'qwe@mailru']

	print(email_parse(test_emails))