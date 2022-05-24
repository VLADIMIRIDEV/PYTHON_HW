sum_cube = 0

for num in [num ** 3 for num in range(1, 1001, 2)]:
    if sum([int(sub_num) for sub_num in str(num)]) % 7 == 0:
        sum_cube += num

print(sum_cube)

num_sum_17 = 0

for num in [num ** 3 + 17 for num in range(1, 1001, 2)]:
    if sum([int(sub_num) for sub_num in str(num)]) % 7 == 0:
        num_sum_17 += num

print(num_sum_17)
