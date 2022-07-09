# 5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
from DV_11_4 import *


class Departament(Storage):
	def __init__(self, total_places, departament):
		super().__init__(total_places, used_places=0, storage_list=[])
		self.departament = departament
		self.departament_allocation = {}

	def add_to_storage(self, device, departament):
		self.departament_allocation.setdefault(self.departament, device.name)
		print(f'{device.name} is allocated in {self.departament}.')
		print(self.departament_allocation)


if __name__ == "__main__":
	pc = PC('PC', '001', 'note', 'ACER', 'development')
	monitor = Monitor('Monitor', '002', '22inch', 'SUMSUNG')
	dep_1 = Departament(10, 'backend_office')
	dep_1.add_to_storage(pc, 'backend_office')
	dep_2 = Departament(10, 'frontend_office')
	dep_2.add_to_storage(monitor, 'frontend_office')

