# 5. Реализовать класс Stationery (канцелярская принадлежность):
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.
class Stationary:
	def __init__(self, title):
		self.title = title

	def draw(self):
		print(f'Start drawing')


class Pen(Stationary):
	def draw(self):
		print(f'Start drawing by {self.title}')


class Pencil(Stationary):
	def draw(self):
		print(f'Start drawing by {self.title}')


class Handle(Stationary):
	def draw(self):
		print(f'Start drawing by {self.title}')


pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
hand = Handle('hand')
hand.draw()