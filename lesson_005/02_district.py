# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
#  подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from district.central_street.house1.room1 import folks as folks_1
from district.central_street.house1.room2 import folks as folks_2
from district.central_street.house2.room1 import folks as folks_3
from district.central_street.house2.room2 import folks as folks_4
from district.soviet_street.house1.room1 import folks as folks_5
from district.soviet_street.house1.room2 import folks as folks_6
from district.soviet_street.house2.room1 import folks as folks_7
from district.soviet_street.house2.room2 import folks as folks_8

folks_list = [folks_1, folks_2, folks_3, folks_4, folks_5, folks_6, folks_7, folks_8]
new_list = []
string = ', '
for i in range(len(folks_list)):
    for n in range(len(folks_list[i])):
        new_list.append(folks_list[i][n])

print('На районе живут', string.join(new_list))



