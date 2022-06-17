# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных
# им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    my_dict = Counter()
    for i in f:
        my_dict[i.split()[0]] += 1

    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
    print(f'Spamer {ip} - {count} times')
    # print(my_dict.most_common(3))