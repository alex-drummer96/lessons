from random import randint


def think_number():
    '''Загадывает 4-ех значное число где каждая цифра уникальна '''
    my_number = []
    for i in range(20):
        '''формируем список уникальных цифр'''
        if i == 0:
            num = randint(1, 9)
        else:
            num = randint(0, 9)
        my_number.append(num)
        if len(my_number) != len(set(my_number)):
            my_number.remove(num)
        if len(my_number) == 4:
            break
    dict_number = {}
    for i in range(4):
        '''защита от неверного порядка прочтения цифр'''
        dict_number[i] = str(my_number[i])
    return dict_number


def check_number(number_version, correct_answer):
    '''Берет заданое игроком число и сверяет его с загаданым'''
    string_dict = correct_answer
    count_bulls = 0
    count_cows = 0
    for i in range(4):
        x = number_version[i]
        if x == string_dict[i]:
            '''Проверка на точное совпадение значения и положения цифры в загаданом числе'''
            count_bulls += 1
        else:
            if x in string_dict.values():
                '''Проверка на вхождение значения цифры в загаданое число'''
                count_cows += 1
    if count_bulls == 4:
        return True
    else:
        print(f'"Быков":{count_bulls}, "Коров": {count_cows}')







