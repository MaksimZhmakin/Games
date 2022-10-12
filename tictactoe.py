def tic_tac_toe():
    '''
    Классическая игра в крестики-нолики. Игроки по очереди вводят координаты ходов

    '''
    import re
    
    field = [
        [' ', '1', '2', '3'],
        ['1', ' ', ' ', ' '],
        ['2', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ']
    ]
    print('\n'.join(map('  '.join, field)))
    while True:
        while True:
            
            x = input(
                'Ход крестика.\nВведите через один пробел координаты клетки для крестика \n(сначала координата по '
                'вертикали, '
                'затем по горизонтали): ')
            
            if re.match(r'^[1-3]\s[1-3]$', x):
                if ' ' in field[int(x[0])][int(x[2])]:
                    field[int(x[0])][int(x[2])] = 'x'
                    print('\n'.join(map('  '.join, field)))
                    if all(['x' in field[1][1], 'x' in field[1][2], 'x' in field[1][3]]) or \
                       all(['x' in field[2][1], 'x' in field[2][2], 'x' in field[2][3]]) or \
                       all(['x' in field[3][1], 'x' in field[3][2], 'x' in field[3][3]]) or \
                       all(['x' in field[1][1], 'x' in field[2][2], 'x' in field[3][3]]) or \
                       all(['x' in field[3][1], 'x' in field[2][2], 'x' in field[3][1]]):
                        print('Крестики выиграли')
                        exit()
                    if not ' ' in field[0][1:] and ' ' not in field[1] and ' ' not in field[2] and ' ' not in field[3]:
                        print('Ничья')
                        exit()
                    
                
                    break
                else:
                    print('\nТут уже занято!\n')
                    continue
                    
            else:
                print('\nНеправильно введены координаты - попробуйте снова\n')
        while True:
            
            x = input('Ход нолика.\nВведите через один пробел координаты клетки для нолика \n(сначала координата по '
                      'вертикали, '
                      'затем по горизонтали): ')
            
            if re.match(r'^[1-3]\s[1-3]$', x):
                if ' ' in field[int(x[0])][int(x[2])]:
                    field[int(x[0])][int(x[2])] = 'o'
                    print('\n'.join(map('  '.join, field)))
                    if all(['o' in field[1][1], 'o' in field[1][2], 'o' in field[1][3]]) or \
                       all(['o' in field[2][1], 'o' in field[2][2], 'o' in field[2][3]]) or \
                       all(['o' in field[3][1], 'o' in field[3][2], 'o' in field[3][3]]) or \
                       all(['o' in field[1][1], 'o' in field[2][2], 'o' in field[3][3]]) or \
                       all(['o' in field[3][1], 'o' in field[2][2], 'o' in field[3][1]]):
                        print('Нолики выиграли')
                        exit()
                    if not ' ' in field[0][1:] and ' ' not in field[1] and ' ' not in field[2] and ' ' not in field[3]:
                        print('Ничья')
                        exit()
                    break
                else:
                    print('\nТут уже занято!\n')      
                    
            else:
                print('\nНеправильно введены координаты - попробуйте снова\n')


tic_tac_toe()
