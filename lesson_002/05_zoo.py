# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
zoo.pop(-3)
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

lion_cell = zoo.index('lion')
lark_cell = zoo.index('lark')
print(f' лев сидит в клетке под номером {lion_cell + 1},'
      f' а жаворонок - {lark_cell + 1}')
