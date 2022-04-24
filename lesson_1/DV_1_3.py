for num in range(1, 101, 1):
    strings_list = list(str(num))
    # print(strings_list)
    if int(strings_list[-1]) == 1 and num != 11:
        print(f'{num} процент')
    elif int(strings_list[-1]) > 1 and int(strings_list[-1]) < 5:
        if 14 >= num > 11:
            print(f'{num} процентов')
        else:
            print(f'{num} процента')
    else:
        print(f'{num} процентов')

