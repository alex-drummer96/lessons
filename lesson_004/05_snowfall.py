# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
def draw_snowflake(x, y, length):
    while y >= 0:
        for i in range(2):
            sd.start_drawing()
            point = sd.get_point(x, y)
            if i == 0:
                snow = sd.snowflake(center=point, length=length)
            else:
                if y > 0:
                    snow = sd.snowflake(center=point, length=length, color=sd.background_color)
                y -= 20
                x -= sd.random_number(-100, 100)
            sd.finish_drawing()
            sd.sleep(.03)
            if sd.user_want_exit():
                break


x_list = []
y_list = []
length_list = []
for n in range(20):
    x = sd.random_number(50, 550)
    y = random.randrange(400, 600, 100)
    length = sd.random_number(10, 100)
    x_list.append(x)
    y_list.append(y)
    length_list.append(length)

N = 20
while N > 0:
    x_0 = x_list[N - 1]
    y_0 = y_list[N - 1]
    length_0 = length_list[N - 1]
    draw_snowflake(x=x_0, y=y_0, length=length_0)
    N -= 1

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


