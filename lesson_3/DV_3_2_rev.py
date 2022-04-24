# 2. * (вместо задачи 1)
# Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
dictionary_eng_rus = {
	'one': 'один',
	'two': 'два',
	'three': 'три',
	'four': 'четыре',
	'five': 'пять',
	'six': 'шесть',
	'seven': 'семь',
	'eight': 'восемь',
	'nine': 'девять',
	'ten': 'десять',
}


def num_translate_adv(eng_num):
	"""
	Translation of strings from English into Russian using a dictionary, considering uppercase letters.
	:param eng_num - number to be translated into russion
	:return: strings of translated text
	"""
	if eng_num.istitle():
		return print(str(dictionary_eng_rus.get(eng_num.lower())).title())
	return print(dictionary_eng_rus.get(eng_num))


num_translate_adv("Three")
num_translate_adv("four")
num_translate_adv("Five")
num_translate_adv("севен")
num_translate_adv("Eleven")
