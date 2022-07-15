import random

_holder = {}
MAX_BUNCHES = 5
MAX_BUNCH_SIZE = 20
_sorted_keys = None


def put_stones():
    '''Расположить камни на игровой поверхности'''
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = random.randint(1, MAX_BUNCH_SIZE)
    _sorted_keys = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    """Взять камни из кучи"""
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_bunches():
    res = []
    for key in _sorted_keys:
        res.append(_holder[key])
    return res


def is_game_over():
    return sum(_holder.values()) == 0
