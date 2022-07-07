# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg



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
figur_name = {1: 'triangle', 2: 'square', 3: "pentagon", 4: "hexagon"}
name = 2 + int(input(f'Выберите какую вигуру хотите нарисовать: {figur_name}'))
colors = color_dict_objects[int(input(f'Выберите цвет из предложеных: {color_dict_name}'))]
point = sd.get_point(200, 200)

polygon(start_point=point, n=name, color=colors)

sd.pause()
