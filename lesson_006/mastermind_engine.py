from random import randint

def think_number():
    '''Загадывает 4-ех значное число где все цифры уникальны, а 1 - > 0'''
    my_key = [0, 1, 2, 3]
    my_value = []
    my_dict = {}
    for i in my_key:
        '''Отличает 1 цифру от остальных'''
        if i == 0:
            num = randint(1, 9)
        else:
            num = randint(0, 9)
        '''Проверка на уникальность'''
        if num in my_value:
            my_key.append(i)
        else:
            my_value.append(num)
            my_dict[i] = str(num)
    sorted(my_dict.keys())
    return my_dict




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







