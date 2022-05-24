# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить
# сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
cube_list = []

for num in range(1, 1001, 2):
    odd_cube = num ** 3
    cube_list.append(odd_cube)
# print(cube_list)

sum_cube = 0

for num in cube_list:
    num_sum = 0
    for sub_num in str(num):
        num_sum += int(sub_num)
    # print(num_sum)
    if num_sum % 7 == 0:
        sum_cube += num
    else:
        sum_cube += 0

print(sum_cube)

for num in range(len(cube_list)):
    cube_list[num] += 17

num_sum_17 = 0

for num in cube_list:
    num_sum = 0
    for sub_num in str(num):
        num_sum += int(sub_num)
    # print(num_sum)
    if num_sum % 7 == 0:
        num_sum_17 += num
    else:
        num_sum_17 += 0

# print(cube_list)

print(num_sum_17)
