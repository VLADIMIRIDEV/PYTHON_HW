# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
# числа деления клеток соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# © geekbrains.ru 20
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
# количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом
# случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
# make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке
class Cell:
	def __init__(self, quantity):
		self.quantity = quantity

	def __str__(self):
		return f'There are {self.quantity} cells'

	def __add__(self, other):
		return f'Sum of the cells is: {self.quantity + other.quantity}'

	def __sub__(self, other):
		if self.quantity >= other.quantity:
			return f'Difference of the cells is: {self.quantity - other.quantity}'
		else:
			return f'Residue is less than 0'

	def __mul__(self, other):
		return f'The result of multiplication is: {self.quantity * other.quantity}'

	def __floordiv__(self, other):
		return f'The result of division (int) is: {self.quantity // other.quantity}'

	def __truediv__(self, other):
		return f'The result of division (float) is: {self.quantity / other.quantity}'

	def make_order(self, cells_quantity_in_row):
		# result = ''.join([
		# 	'*\\n' if i % cells_quantity_in_row == 0 and i < self.quantity else '*'
		# 	for i in range(1, self.quantity + 1)])
		# return result
		return '\\n'.join(
			['*' * cells_quantity_in_row for _ in range(self.quantity // cells_quantity_in_row)]
		) + "\\n" + '*' * (self.quantity % cells_quantity_in_row)


if __name__ == '__main__':
	cell_1 = Cell(12)
	cell_2 = Cell(15)
	print(cell_1 + cell_2)
	print(cell_1 - cell_2)
	print(cell_1 * cell_2)
	print(cell_1 // cell_2)
	print(cell_1 / cell_2)
	print(cell_1.make_order(5))
	print(cell_2.make_order(5))