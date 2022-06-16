# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу
# со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

from sys import argv
from itertools import zip_longest

user, hobby, out_file = argv[1:]

with open(user, 'r', encoding='utf-8') as users:
    with open(hobby, 'r', encoding='utf-8') as hobbies:
        all_list = zip_longest((' '.join(user.split(',')) for user in users), hobbies, fillvalue=None)

        with open(out_file, 'w', encoding='utf-8') as f:
            for i in all_list:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=f)
