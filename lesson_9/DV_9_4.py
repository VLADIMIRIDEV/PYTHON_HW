# 4. Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.
class Car:
	def __init__(self, name, color, speed, is_police=False):
		self.name = name
		self.color = color
		self.speed = speed
		self.police = is_police

	def go(self):
		return f'The {self.name} is going.'

	def stop(self):
		return f'The {self.name} has stopped.'

	def turn(self, direction):
		return f'The {self.name} is turning to the {direction}.'

	def speed_show(self):
		return f'The speed is {self.speed}.'


class TownCar(Car):
	def speed_show(self):
		if self.speed > 60:
			return f'Slow down! Your speed is too fast.'
		else:
			return f'Go on'


class WorkCar(Car):
	def speed_show(self):
		if self.speed > 40:
			return f'Slow down! Your speed is too fast.'
		else:
			return f'Go on.'


town = TownCar('Chevy', 'black', 90, False)
print(town.go(), town.speed_show(), town.turn('left'), town.turn('right'), town.stop(), sep='\n', end='\n\n')
work = WorkCar('GAZ', 'white', 40, False)
print(work.go(), work.speed_show(), work.turn('left'), work.turn('right'), work.stop(), sep='\n', end='\n\n')