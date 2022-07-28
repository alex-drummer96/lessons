# -*- coding: utf-8 -*-

from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:
    def __init__(self, name):
        self.fullness = 50
        self.name = name
        self.house = None
        self.cat_name = None

    def __str__(self):
        return f'I am - {self.name}, fullness - {self.fullness},'

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} ate')
            self.fullness += 10
            self.house.food -= 10
        else:
            print(f'{self.name} has no food')

    def work(self):
        print(f'{self.name} went to work')
        self.house.money += 150
        self.fullness -= 10

    def play_game(self):
        print(f'{self.name} played games')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} went shopping')
            self.house.money -= 50
            self.house.food += 50
        else:
            print('No money - No honey')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20

    def buy_cat_food(self):
        if self.house.money >= 50:
            print(f'{self.name} going to buy cat food')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            print('No money - No honey')

    def settle_in_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} settle in a house')

    def pick_up_cat(self, house, cat_name):
        self.house = house
        self.cat_name = cat_name
        self.fullness -= 10
        self.cat_name.house = house
        print(f'Now the cat {self.cat_name.name} lives in the house')

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} died')
            return False
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_game()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50
        self.cat_food = 10
        self.dirt = 0

    def __str__(self):
        return f"В доме осталось еды для человека:{self.food} и для кота: {self.cat_food}," \
               f" в доме соталось денег: {self.money}. Уровень грязи в доме: {self.dirt}"


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def sleep(self):
        self.fullness -= 10
        print(f'cat {self.name} is sleeping')

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        print(f'cat {self.name} ate')

    def rip_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        print(f'cat {self.name} skinned wallpaper')

    def act(self):
        if self.fullness <= 0:
            print(f'cat {self.name} died')
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.rip_wallpaper()
        else:
            self.sleep()

    def __str__(self):
        return f'I am cat {self.name}, fullness: {self.fullness}'


house1 = House()
sasha = Man(name='Sasha')
murzick = Cat(name='Murzick')
sasha.settle_in_house(house=house1)
sasha.pick_up_cat(house=house1, cat_name=murzick)
for day in range(1, 366):
    print(f'===================={day}==============================')
    sasha.act()
    murzick.act()
    print(house1)
    print(sasha)
    print(murzick)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
