# 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
class Storage:
	def __init__(self, total_places, used_places=0, storage_list=[]):
		self.total_places = total_places
		self.used_places = used_places
		self.storage_list = storage_list

	def add_to_storage(self, device):
		self.storage_list.append(device)
		self.used_places += 1
		print(f'{device.name} is added. There are {self.total_places - self.used_places} free places left.')


class Devices:
	def __init__(self, name, number):
		self.name = name
		self.number = number


class PC(Devices):
	def __init__(self, name, number, type_of_pc, brand, purpose):
		super().__init__(name, number)
		self.type_of_pc = type_of_pc
		self.brand = brand
		self.purpose = purpose

	def print_text(self, text):
		print(f'{text} {self.type_of_pc} {self.brand} for {self.purpose}.')


class Monitor(Devices):
	def __init__(self, name, number, diagonal, brand):
		super().__init__(name, number)
		self.diagonal = diagonal
		self.brand = brand

	def print_text(self, text):
		print(f'{text} {self.name} {self.diagonal} {self.brand}.')


if __name__ == "__main__":
	storage = Storage(20)
	pc = PC('PC', '001', 'note', 'ACER', 'development')
	pc.print_text('I have bought')
	monitor = Monitor('Monitor', '002', '22inch', 'SUMSUNG')
	monitor.print_text('I need to buy')
	storage.add_to_storage(pc)
	storage.add_to_storage(monitor)