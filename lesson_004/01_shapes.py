# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(start_point, angle, length):
#     for i in range(3):
#         v = sd.get_vector(start_point=start_point, length=length, angle=angle, width=2)
#         v.draw()
#         start_point = v.end_point
#         angle += 120
#
# def square(start_point, angle, length):
#     for i in range(4):
#         v = sd.get_vector(start_point=start_point, length=length, angle=angle, width=2)
#         v.draw()
#         start_point = v.end_point
#         angle += 90
#
# def pentagon(start_point, angle, length):
#     for i in range(5):
#         v = sd.get_vector(start_point=start_point, length=length, angle=angle, width=2)
#         v.draw()
#         start_point = v.end_point
#         angle += 72
#
# def hexagon(start_point, angle, length):
#     for i in range(6):
#         v = sd.get_vector(start_point=start_point, length=length, angle=angle, width=2)
#         v.draw()
#         start_point = v.end_point
#         angle += 60
#
# point_triangle = sd.get_point(300, 300)
# point_square = sd.get_point(150, 150)
# point_pentagon = sd.get_point(400, 50)
# point_hexagon = sd.get_point(70, 350)
#
# triangle(start_point=point_triangle, angle=0, length=140)
# square(start_point=point_square, angle=0, length=140)
# pentagon(start_point=point_pentagon, angle=0, length=140)
# hexagon(start_point=point_hexagon, angle=0, length=140)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)
# def polygon(start_point, number, angle=0, length=140):
#     for i in range(1, number):
#         v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
#         v.draw()
#         start_point = v.end_point
#         angle += 360 / number
#
#
# point = sd.get_point(300, 300)
# n = print(int(input('введите количество углов фигуры')))
# polygon(start_point=point, number=n)

def polygon(start_point, number, angle=0, length=140):
    for i in range(number):
        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
        v.draw()
        start_point = v.end_point
        angle += 360 / number


def print_figure(quantity):
    start_x = 10
    start_y = 10
    for figure in range(1, quantity + 1):
        point = sd.get_point(start_x, start_y)
        if start_x <= 400:
            start_x += 200
        elif start_x >= 400:
            start_y += 300
            start_x -= 50
        polygon(start_point=point, number=figure+2)
quantity = int(input("Сколько фигур вы хотите напечатать?"))

print_figure(quantity=quantity)
# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
