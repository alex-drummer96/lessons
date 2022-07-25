# # -*- coding: utf-8 -*-
#
import simple_draw as sd
from random import randint

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.snow = None
        self.x = randint(100, 1000)
        self.y = randint(450, 600)
        self.length = randint(10, 100)

    def draw(self):
        self.snow = sd.snowflake(center=sd.get_point(x=self.x, y=self.y), length=self.length,
                                 color=sd.COLOR_WHITE)

    def move(self):
        self.y -= 5
        self.x -= randint(-20, 20)

    def clear_previous_picture(self):
        self.snow = self.snow = sd.snowflake(center=sd.get_point(x=self.x, y=self.y), length=self.length,
                                             color=sd.background_color)

    def can_fall(self):
        if self.y > 0:
            return True


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
