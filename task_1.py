x = [1, [2]]
y = x.copy()
y[1] = 2


def iss(x, y):
    if x is y and x == y:
        print('Две переменные ссылаются на один и тот же адрес в памяти, имеют одинаковые значения.')
        print(f'id первой переменной: ', id(x))
        print(f'id второй переменной: ', id(y))
        print(f'Значение первой переменной: ', x)
        print(f'Значение второй переменной: ', y)
    if x is not y and x == y:
        print('Две переменные ссылаются на разные адреса в памяти, имеют одинаковые значения.')
        print(f'id первой переменной: ', id(x))
        print(f'id второй переменной: ', id(y))
        print(f'Значение первой переменной: ', x)
        print(f'Значение второй переменной: ', y)
    if x is not y and x != y:
        print('Две переменные ссылаются на разные адреса в памяти, имеют разные значения.')
        print(f'id первой переменной: ', id(x))
        print(f'id второй переменной: ', id(y))
        print(f'Значение первой переменной: ', x)
        print(f'Значение второй переменной: ', y)


iss(x, y)