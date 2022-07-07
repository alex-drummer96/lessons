# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def polygon(start_point, n, color, angle=0, length=140):
    for i in range(n):
        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
        v.draw(color=color)
        start_point = v.end_point
        angle += 360 / n


color_dict_objects = {0: sd.COLOR_RED, 1: sd.COLOR_ORANGE, 2: sd.COLOR_YELLOW, 3: sd.COLOR_GREEN, 4: sd.COLOR_CYAN,
                      5: sd.COLOR_BLUE, 6: sd.COLOR_PURPLE}
color_dict_name = {0: 'COLOR_RED', 1: 'COLOR_ORANGE', 2: 'COLOR_YELLOW', 3: 'COLOR_GREEN', 4: 'COLOR_CYAN',
                   5: 'COLOR_BLUE', 6: 'COLOR_PURPLE'}
colors = color_dict_objects[int(input(f'Выберите цвет из предложеных: {color_dict_name}'))]
quantity = int(input("Сколько фигур вы хотите напечатать?"))
start_x = 10
start_y = 10
for figure in range(1, quantity + 1):
    point = sd.get_point(start_x, start_y)
    if start_x <= 400:
        start_x += 200
    elif start_x >= 400:
        start_y += 300
        start_x -= 50
    polygon(start_point=point, n=figure + 2, color=colors)

sd.pause()
