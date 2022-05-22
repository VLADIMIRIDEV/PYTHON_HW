# 4. * (вместо задачи 3)
# Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и
# возвращающую словарь, в котором ключи — первые буквы фамилий, а
# значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых
# фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?
""" """


def get_first_surname(*args):
	"""
	Way # 1: Making dict from names sorted by keys, where a key of dict is the first letter of a surname and a key of a subdict is the first letter of name/
	:param args: list of strings those contain name and surname
	:return: dict of dicts
	"""
	fl_dict = {}
	for name in sorted(args):
		n, s = name.split()
		val = fl_dict.setdefault(s[0], {n[0]: [name]})
		n_val = val.setdefault(n[0], [name])
		if name not in n_val:
			n_val.append(name)
	return fl_dict


def get_first_surname_letter(*args):
	"""
	Way # 2: Making dict from names sorted by keys, where a key of dict is the first letter of a surname and a key of a subdict is the first letter of name/
	:param args: list of strings those contain name and surname
	:return: dict of dicts
	"""
	fl_dict = {}
	for s_name in sorted(args):
		fl_dict.setdefault(s_name.split()[1][0], {}).setdefault(s_name.split()[0][0], []).append(s_name)
	return fl_dict


names = [
	'Владимир Долгополов',
	'Ольга Долгополова',
	'Вероника Долгополова',
	'Вова Долгополов',
	'Мария Долгополова',
	'Нина Грибова',
	'Илья Долгополов',
	'Анатолий Грибов'
]
print(get_first_surname(*names))
print(get_first_surname_letter(*names))
