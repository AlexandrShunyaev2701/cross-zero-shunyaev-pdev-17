
maps = [[' ',' ',' '] for i in range(3)] #Создаем игровое поле
# Выйгрышные комбинации(по строкам, по столбам и диагоналям)
s_1 = ((0, 0), (0, 1), (0, 2))
s_2 = ((1, 0), (1, 1), (1, 2))
s_3 = ((2, 0), (2, 1), (2, 2))
col_1 = ((0, 0), (1, 0), (2, 0))
col_2 = ((0, 1), (1, 1), (2, 1))
col_3 = ((0, 2), (1, 2), (2, 2))
dia_1 = ((0, 0), (1, 1), (2, 2))
dia_2 = ((2, 0), (1, 1), (0, 2))
win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))


def print_maps(): # Печатаем игровое поле с приветствием
    print(f'  0  1  2')
    for i in range(3):
        print(f'{i} {maps[i][0]}  {maps[i][1]}  {maps[i][2]}')
    return ''
# Поверка выйграшной комбинации
def if_win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for i in win_comb:
        win_list = []
        for j in i:
            win_list.append(maps[j[0]][j[1]])
            if win_list == ['X', 'X', 'X']:
                print('Победили Х')
                return True
            if win_list == ['O', 'O', 'O']:
                print('Победили О')
                return True
    return False

def step_x():  #Делаем ход X
    print('Ходят Х')
    step = list(map(int, input('Ход ')))
    m1 = step[0]
    m2 = step[1]
    maps[m1][m2] = 'X'

def step_o():   #Делают ход О
    print('Ходят О')
    step = list(map(int, input('Ход ')))
    m1 = step[0]
    m2 = step[1]
    maps[m1][m2] = 'O'

    
def play(): #Запускаем саму игру
    Hello = input("Готовы начать игру? y/n? ")
    if Hello == 'y':
        print('Это игра в крестики - нолики. Вводить нужно координаты хода(сначала строку потом столбец без пробела). '
            'Первые ходят Х.')
        print_maps()
        for i in range(1, 6):
            step_x()
            print_maps()
            if_win()
            if if_win():
                break
            if i == 5 and not if_win():
                print('Ничья')
                break
            step_o()
            print_maps()
            if if_win():
                break
        return print('GAME OVER')
    else:
        print('Нет так нет. До встречи!')


play()









