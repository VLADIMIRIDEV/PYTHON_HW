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

test_emails = ['allisposible@mail.ru', 'someone@geekbrainsru', 'cumba@bk.ru', 'qwe@mailru']

EMAIL = re.compile(r'(?P<username>[a-zA-Z0-9]+[_.-]*[a-zA-Z0-9]+)@(?P<domain>[a-z]+\.[a-z]{2,})')


def email_parse(address):
	match = re.search(EMAIL, address)
	if not match:
		raise ValueError (f'wrong email: {address}')
	return match.groupdict()


res = map(email_parse, test_emails)
for r in res:
	print(r)
