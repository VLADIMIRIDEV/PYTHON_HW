# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
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


def num_translate(eng_num, dictionary):
	"""
	Translation of string from English into Russian using a dictionary
	:param eng_num - number to be translated into russion
	:param dictionary - dictionary to be used for translating
	:return: translating result
	"""
	translated_result = dictionary.get(eng_num, None)
	return translated_result


print(num_translate('one', dictionary_eng_rus))
print(num_translate('eight', dictionary_eng_rus))
print(num_translate('eleven', dictionary_eng_rus))