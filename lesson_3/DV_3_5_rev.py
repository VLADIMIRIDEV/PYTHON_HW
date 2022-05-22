# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
from random import choice, randrange


def get_jokes(num, repeat=False):
    """
    Joke generation function returns num jokes from three random words - one from each list.
    :param num: num of jokes
    :param repeat: True/False
    :return: a list of jokes
    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    joke_list = []
    joke_list_min = min(no, adv, adj)

    while num and len(joke_list_min):
        n = randrange(len(joke_list_min))
        if repeat:
            joke_list.append(f'{no.pop(n)} {adv.pop(n)} {adj.pop(n)}')
        else:
            joke_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        num -= 1
    return joke_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(100, True))
print(get_jokes(10))




