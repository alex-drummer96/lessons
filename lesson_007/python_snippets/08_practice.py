from random import randint
from termcolor import cprint


class Man:
    def __init__(self, name):
        self.fullness = 50
        self.name = name
        self.house = None

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
        self.house.money += 50
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

    def settle_in_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} settle in a house')

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} died')
            return False
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
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

    def __str__(self):
        return f"В доме осталось еды:{self.food}, в доме соталось денег: {self.money}"

beavis = Man(name='Beavis')
butthead = Man(name='Butthead')
house1 = House()
beavis.settle_in_house(house=house1)
butthead.settle_in_house(house=house1)

for day in range(1, 366):
    cprint(f'******************************** DAY: {day} *******************************', color='yellow')
    beavis.act()
    butthead.act()
    cprint(f'*********************** at the end of the day: {day} ***********************', color='yellow')
    cprint(house1, color='magenta')
    cprint(beavis, color='blue')
    cprint(butthead, color='green')


