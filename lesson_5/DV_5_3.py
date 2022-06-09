# 3. Есть два списка:
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
# например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
# списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
# кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.
#
# Way 1
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Владимир', 'Вероника']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klasses_dict = {index: klass for index, klass in enumerate(klasses)}
# print(klasses_dict)
my_gen = ((tutor, klasses_dict.get(index)) for index, tutor in zip(range(len(tutors)), tutors))

print(type(my_gen))
print(*my_gen, sep='\n')
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

# Way 2
def tup_gen(tutors, klasses):
	return ((tutor, klasses[index]) if index < len(klasses) else (tutor, None)
			for index, tutor in enumerate(tutors))


if __name__ =='__main__':

	tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Мария']
	klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

	gen = tup_gen(tutors, klasses)
	print(type(gen))
	print(*gen, sep='\n')