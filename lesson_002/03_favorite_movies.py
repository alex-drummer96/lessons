# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов
from pprint import pprint

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

print(f'{my_favorite_movies[0:10]}\n{my_favorite_movies[-15:-1]}\n{my_favorite_movies[12:25]}'
      f'\n{my_favorite_movies[-22:-17]}')
