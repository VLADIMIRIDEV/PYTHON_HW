# 7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
# число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
# выполнить сложение и умножение созданных экземпляров. Проверить корректность
# полученного результата.
import math


class ComplexNum:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.x = complex(a, b)
		print(f'Complex number {self.x}.')

	def __add__(self, other):
		return f'sum of {self.x} and {other.x}: ' \
		       f'{complex((self.a + other.a), (self.a + other.a))}'

	def __mul__(self, other):
		return f'mul of {self.x} and {other.x}: ' \
		       f'{complex((self.a * other.a), (self.a * other.a))}'


if __name__ == "__main__":
	num_1 = ComplexNum(1, 2)
	num_2 = ComplexNum(3, 4)
	print(num_1 + num_2)
	print(num_1 * num_2)