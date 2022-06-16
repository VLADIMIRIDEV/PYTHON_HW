# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение.
# При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as count:
	pos, val = argv[1:]
	val = round(float(val.replace(',', '.')), 2)
	for line in range(int(pos)):
		p = count.tell()
		print(p)
		n = count.readline().strip()
		if n == '':
			exit('Error: there is not the string')

	if ',' in str(val) or '.' in str(val):
		if val <= 99999.999:
			count.seek(p)
			count.write(f'{val:>10}')
		else:
			print('Number nust be less than 99 999,999')