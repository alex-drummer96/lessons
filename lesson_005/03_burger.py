# -*- coding: utf-8 -*-
import my_burger
# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

def burger():
    my_burger.bun()
    my_burger.mayonnaise()
    my_burger.cheese()
    my_burger.cutlet()
    my_burger.cucumber()
    my_burger.tomato()
    my_burger.cheese()
    my_burger.mayonnaise()


burger()

def crabsburger():
    print("Делаем Крабсбургер")
    my_burger.bun()
    my_burger.cutlet()
    my_burger.cheese()
    my_burger.mayonnaise()
    my_burger.tomato()
    my_burger.cucumber()
    my_burger.onion()
    my_burger.ketchup()
    my_burger.secret_sauce()

crabsburger()