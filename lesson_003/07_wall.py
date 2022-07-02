# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
red = simple_draw.COLOR_RED

lef_y = -50
for y in range(15):
    lef_y += 50
    right_y = lef_y + 50
    lef_x = -(y * 50)
    for x in range(20):
        right_x = lef_x + 100
        left_bottom = simple_draw.get_point(lef_x, lef_y)
        right_top = simple_draw.get_point(right_x, right_y)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=red, width=2)
        lef_x += 100

simple_draw.pause()
