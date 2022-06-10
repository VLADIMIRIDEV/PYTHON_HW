# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.


def odd_nums_1(n):
	for num in range(1, n + 1, 2):
		yield num


def odd_nums_2(n):
	return (num for num in range(1, n + 1, 2))


if __name__ == '__main__':
	nums_1 = odd_nums_1(3)
	nums_2 = odd_nums_2(3)
	print(next(nums_1, None))
	print(next(nums_1, None))
	print(next(nums_1, None))
	print(next(nums_2, None))
	print(next(nums_2, None))
	print(next(nums_2, None))


