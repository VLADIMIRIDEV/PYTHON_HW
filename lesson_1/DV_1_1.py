# 1. Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
# Примечание: можете проверить себя здесь, подумайте, можно ли
# использовать цикл для проверки работы кода сразу для нескольких
# значений продолжительности, будет ли тут полезен список?
duration = int(input())
days = duration // (60*60*24)
hours = (duration - days * (60*60*24)) // 3600
minutes = (duration - days * (60*60*24) - hours * 3600) // 60
seconds = duration - days * (60*60*24) - hours * 3600 - minutes * 60
if days > 0:
  print(f'{days} дн {hours} ч {minutes} мин {seconds} сек')
elif days <= 0 and hours > 0:
  print(f'{hours} чаc {minutes} мин {seconds} сек')
elif days <= 0 and hours < 0:
  print(f'{minutes} мин {seconds} сек')
else:
  print(f'{seconds} сек')
