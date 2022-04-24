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
