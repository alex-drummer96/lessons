# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
import random


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    '''рисуем большой круг'''
    point = simple_draw.get_point(x, y)
    radius = 60
    simple_draw.circle(center_position=point, radius=radius, color=color, width=2)
    little_x = x - radius / 2
    little_y = y + radius / 2
    for _ in range(2):
        ''' рисуем глаза'''
        little_point = simple_draw.get_point(little_x, little_y)
        simple_draw.circle(center_position=little_point, radius=6, color=color, width=1)
        little_x += radius
    smile_x = x - radius / 2
    smile_y = y - radius / 2
    smile_list = []
    for n in range(4):
        """ рисуем улыбку"""
        smile_point = simple_draw.get_point(smile_x, smile_y)
        smile_list.append(smile_point)
        smile_x += radius / 3
        if n < 1:
            smile_y -= radius / 4
        elif 1 >= n <= 2:
            pass
        else:
            smile_y += radius / 4
    simple_draw.lines(point_list=smile_list, color=color, closed=False, width=2)


color = simple_draw.COLOR_YELLOW
for i in range(10):
    x = random.randrange(600)
    y = random.randrange(600)
    smile(x, y, color)

simple_draw.pause()
