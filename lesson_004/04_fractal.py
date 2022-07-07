# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 700)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
point_0 = sd.get_point(600, 0)

def draw_branches(start_point, angle, length):
    if length > 3:
        coefficient = 0.75
        delta = 30
        next_length = length * coefficient
        v0 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
        v0.draw()
        next_point = v0.end_point
        next_angle = angle - delta
        for i in range(2):
            draw_branches(start_point=next_point, angle=next_angle, length=next_length)
            next_angle = angle + delta


draw_branches(start_point=point_0, angle=90, length=150)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
#
point_0 = sd.get_point(600, 0)


def draw_branches(start_point, angle, length):
    if length > 3:
        coefficient = random.randint(60, 90) / 100
        delta = random.randint(18, 42)
        next_length = length * coefficient
        v0 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
        v0.draw(sd.COLOR_RED)
        next_point = v0.end_point
        next_angle = angle - delta
        for i in range(2):
            draw_branches(start_point=next_point, angle=next_angle, length=next_length)
            next_angle = angle + delta


draw_branches(start_point=point_0, angle=90, length=150)

# Пригодятся функции
# sd.random_number()

sd.pause()
