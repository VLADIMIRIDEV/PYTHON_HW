# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

from pickle import dump, load
from itertools import zip_longest

# ________________________________________________________________________ 1 varian

# with open('users.csv', 'r', encoding='utf-8') as users:
#     with open('hobbies.csv', 'r', encoding='utf-8') as hobbies:
#
#         if len(users.readlines()) >= len(hobbies.readlines()): # считываем всю информацию и измеряем ее длинну
#             users.seek(0) # перемещаем курсор в начало
#             hobbies.seek(0)
#             with open('dict_user_hobby.pickle', 'wb') as f:
#                 all_list = zip_longest((' '.join(user.split(',')) for user in users), hobbies, fillvalue=None)
#                 my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}
#
#                 dump(my_dict, f)
#             print(my_dict)
#         else:
#             exit(1)

# ________________________________________________________________________ 2 varian

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobbies.csv', 'r', encoding='utf-8') as hobbies:
        all_list = zip_longest((' '.join(user.split(',')) for user in users), hobbies, fillvalue=None)
        my_dict = {str(el[0]).strip(): (str(el[1]).strip()) if el[0] else exit(1) for el in all_list}

        with open('dict_user_hobby.pickle', 'wb') as f:
            dump(my_dict, f)
            # print(my_dict)

with open('dict_user_hobby.pickle', 'rb') as f:
    print(load(f))