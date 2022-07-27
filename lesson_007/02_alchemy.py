# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.name = 'water'

    def __add__(self, other):
        if other.name == 'air':
            new_obj = Storm()
            return new_obj
        elif other.name == 'fire':
            new_obj = Steam()
            return new_obj
        elif other.name == 'ground':
            new_obj = Dirt()
            return new_obj
        else:
            return None

    def __str__(self):
        return self.name


class Air:

    def __init__(self):
        self.name = 'air'

    def __add__(self, other):
        if other.name == 'water':
            new_obj = Storm()
            return new_obj
        elif other.name == 'fire':
            new_obj = Lightning()
            return new_obj
        elif other.name == 'ground':
            new_obj = Dust()
            return new_obj
        else:
            return None

    def __str__(self):
        return self.name


class Fire:

    def __init__(self):
        self.name = 'fire'

    def __add__(self, other):
        if other.name == 'air':
            new_obj = Lightning()
            return new_obj
        elif other.name == 'water':
            new_obj = Steam()
            return new_obj
        elif other.name == 'ground':
            new_obj = Lava()
            return new_obj
        else:
            return None

    def __str__(self):
        return self.name


class Ground:

    def __init__(self):
        self.name = 'ground'

    def __add__(self, other):
        if other.name == 'air':
            new_obj = Dust()
            return new_obj
        elif other.name == 'fire':
            new_obj = Lava()
            return new_obj
        elif other.name == 'water':
            new_obj = Dirt()
            return new_obj
        else:
            return None

    def __str__(self):
        return self.name


class Storm:

    def __init__(self):
        self.name = 'storm'

    def __str__(self):
        return self.name


class Steam:

    def __init__(self):
        self.name = 'steam'

    def __str__(self):
        return self.name


class Dirt:

    def __init__(self):
        self.name = 'dirt'

    def __str__(self):
        return self.name


class Lightning:

    def __init__(self):
        self.name = 'lightning'

    def __str__(self):
        return self.name


class Dust:

    def __init__(self):
        self.name = 'dust'

    def __str__(self):
        return self.name


class Lava:

    def __init__(self):
        self.name = 'lava'

    def __str__(self):
        return self.name


print(Water() + Air())
print(Water() + Fire())
print(Water() + Ground())
print(Air() + Water())
print(Air() + Fire())
print(Air() + Ground())
print(Fire() + Water())
print(Fire() + Air())
print(Fire() + Ground())
print(Ground() + Fire())
print(Ground() + Air())
print(Ground() + Water())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
