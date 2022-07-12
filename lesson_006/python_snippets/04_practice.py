# -*- coding: utf-8 -*-


# Ним — математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трём.

# Составить модуль, реализующий функциональность игры.
# Функции управления игрой
#  разложить_камни()
#  взять_из_кучи(NN, KK)
#  положение_камней() - возвращает список [XX, YY, ZZ, ...] - текущее расположение камней
#  есть_конец_игры() - возвращает True если больше ходов сделать нельзя
#
#
# В текущем модуле (lesson_006/python_snippets/04_practice.py) реализовать логику работы с пользователем:
#  начало игры,
#  вывод расположения камней
#  ввод первым игроком хода - позицию и кол-во камней
#  вывод расположения камней
#  ввод вторым игроком хода - позицию и кол-во камней
#  вывод расположения камней

from nim_engine import put_stones, get_bunches, take_from_bunch, is_game_over
from termcolor import cprint, colored

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'red' if user_number == 1 else 'blue'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input(colored('Откуда будете брать?', color=user_color))
    qua = input(colored('Сколько будете брать?', color=user_color))
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_game_over():
        break
    user_number = 2 if user_number == 1 else 1
cprint(f'Победил игрок {user_number}', color='magenta')
