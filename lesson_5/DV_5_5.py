# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

from time import perf_counter

# Way 1
start = perf_counter()
result = []
for el in src:
	if src.count(el) == 1:
		result.append(el)
print('Способ 1', type(result))
print(result, perf_counter() - start)

# Way 1 Comprehension
start = perf_counter()
result = [el for el in src if src.count(el) == 1]
print('Способ 2', type(result))
print(result, perf_counter() - start)

# Way 2 - faster
start = perf_counter()
not_repeat_src = set()
repeat_src = set()
for el in src:
	if el not in repeat_src:
		not_repeat_src.add(el)
	else:
		not_repeat_src.discard(el)
	repeat_src.add(el)
print('Способ 3', type(not_repeat_src))
not_repeat_src_ord = [el for el in src if el in not_repeat_src]
print(not_repeat_src_ord, perf_counter() - start)