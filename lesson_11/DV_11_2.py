# 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DivisionError(Exception):
	def __init__(self, txt):
		self.txt = txt


num_1, num_2 = input('input number: '), input('input number: ')

try:
	num_1 = int(num_1)
	num_2 = int(num_2)
	if num_2 == 0:
		raise DivisionError("You can't divide by zero.")
	else:
		print(num_1 / num_2)
except ValueError:
	print('You must input integer.')