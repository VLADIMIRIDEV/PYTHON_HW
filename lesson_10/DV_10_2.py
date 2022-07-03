# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
# знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
# декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
	def __init__(self, param):
		self.param = param

	@abstractmethod # абстрактный метод, который будет необходимо переопределять для каждого подкласса
	def abstract(self):
		return 'Abstract'


class Coat(Clothes):
	def __init__(self, param, v):
		super().__init__(param)
		self.v = v

	@property
	def fabric_consumption(self):
		return f'It will need to make a {self.param}: {self.v / 6.5 + 0.5:.2f} metre fabric'

	def abstract(self):
		return 'Abstract 2'


class Suit(Clothes):
	def __init__(self, param, h):
		super().__init__(param)
		self.h = h

	@property
	def fabric_consumption(self):
		return f'It will need to make a {self.param}: {2 * self.h + 0.3:.2f} metre fabric'

	def abstract(self):
		return 'Abstract 3'


if __name__ == '__main__':
	coat = Coat('Coat', 52)
	suit = Suit('Suit', 1.82)
	print(coat.fabric_consumption) # with @property
	print(suit.fabric_consumption) # with @property
	# print(coat.fabric_consumption()) # without @property
	# print(suit.fabric_consumption()) # without @property
	print(coat.abstract())
	print(suit.abstract())