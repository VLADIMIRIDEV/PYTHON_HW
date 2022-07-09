# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

from datetime import datetime


class Data:
	def __init__(self, date_text):
		self.date_text = date_text

	@classmethod
	def get_int_date(cls, date_text):
		d, m, y = [int(i) for i in date_text.split('-')]
		return d, m, y

	@staticmethod
	def validate(date_text):
		try:
			datetime.strptime(date_text, '%d-%m-%Y')
		except ValueError:
			raise ValueError("Incorrect data format, should be DD-MM-YYYY")


print(Data.get_int_date('07-07-2022'))
print(Data.validate('31-13-2022'))