def tup_gen(tutors, klasses):
	i = 0
	while i < len(tutors) and i < len(klasses):
		yield (tutors[i], klasses[i])
		i += 1
	while i < len(tutors):
		yield (tutors[i], None)
		i += 1
	while i < len(klasses):
		yield (None, klasses[i])
		i += 1

if __name__ =='__main__':

	tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Мария']
	klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

	gen = tup_gen(tutors, klasses)
	print(type(gen))
	for tup in tup_gen(tutors, klasses):
		print(tup)
