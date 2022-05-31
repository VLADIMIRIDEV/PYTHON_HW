# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором
# ключи — первые буквы имён, а
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте:
# полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*args):
	"""
	Making dict from names sorted by keys, where key is the first letter of a name
	:param args: names
	:return: dict
	"""
	names_dict = {}
	for name in sorted(args):
		key = name[0].capitalize()
		if key not in names_dict:
			names_dict[key] = []
		names_dict[key].append(name)
	# sorted_names_dict = dict(sorted(names_dict.items()))
	# print(sorted_names_dict)
	# return sorted_names_dict
	return names_dict


names = ['Владимир',
		 'Ольга',
		 'Вероника',
		 'Вова',
		 'Мария',
		 'Нина',
		 'Илья',
		 'Анатолий']

print(thesaurus(*names))