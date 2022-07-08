goods = {
    'Стул': '45678'
}
store = {
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for name, code in goods.items():
    local_quantity = 0
    local_price = 0
    total_quantity = 0
    total_cost = 0
    for some_dict in store[code]:
        for key in some_dict:
            if key == 'quantity':
                local_quantity = some_dict[key]
            else:
                local_price = some_dict[key]
        total_quantity += local_quantity
        total_cost += local_quantity * local_price
    print(name, '-', total_quantity, 'шт, стоимость', total_cost, 'руб')