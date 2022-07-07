# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200

length = 200
point = sd.get_point(300, 300)


# v1 = sd.get_vector(start_point=point, angle=0, length=length, width=2)
# v1.draw()
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=length, width=2)
# v2.draw()
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=length, width=2)
# v3.draw()

# определить функцию рисования треугольника из заданной точки с заданным наклоном

def triangle(point, angle=0):
    color = sd.COLOR_PURPLE
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=2)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=2)
    v3.draw(color=color)


for angle in range(0, 361, 30):
    triangle(point, angle)

sd.pause()
