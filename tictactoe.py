def match(sample):
    import re
    return re.match(r'^[1-3]\s[1-3]$', sample)

def tic_tac_toe():
    '''
    Классическая игра в крестики-нолики. Игроки по очереди вводят координаты ходов

    '''
    
    
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
            
            if match(x):
                if ' ' in field[int(x[0])][int(x[2])]:
                    field[int(x[0])][int(x[2])] = 'x'
                    print('\n'.join(map('  '.join, field)))
                    if 'x' in [field[1][1]] and 'x' in [field[1][2]] and 'x' in [field[1][3]] or \
                            'x' in [field[2][1]] and 'x' in [field[2][2]] and 'x' in [field[2][3]] or \
                            'x' in [field[3][1]] and 'x' in [field[3][2]] and 'x' in [field[3][3]] or \
                            'x' in [field[1][1]] and 'x' in [field[2][1]] and 'x' in [field[3][1]] or \
                            'x' in [field[1][2]] and 'x' in [field[2][2]] and 'x' in [field[3][2]] or \
                            'x' in [field[1][3]] and 'x' in [field[2][3]] and 'x' in [field[3][3]] or \
                            'x' in [field[1][1]] and 'x' in [field[2][2]] and 'x' in [field[3][3]] or \
                            'x' in [field[3][1]] and 'x' in [field[2][2]] and 'x' in [field[1][3]]:
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
            
            if match(x):
                if ' ' in field[int(x[0])][int(x[2])]:
                    field[int(x[0])][int(x[2])] = 'o'
                    print('\n'.join(map('  '.join, field)))
                    if 'o' in [field[1][1]] and 'o' in [field[1][2]] and 'o' in [field[1][3]] or \
                            'o' in [field[2][1]] and 'o' in [field[2][2]] and 'o' in [field[2][3]] or \
                            'o' in [field[3][1]] and 'o' in [field[3][2]] and 'o' in [field[3][3]] or \
                            'o' in [field[1][1]] and 'o' in [field[2][1]] and 'o' in [field[3][1]] or \
                            'o' in [field[1][2]] and 'o' in [field[2][2]] and 'o' in [field[3][2]] or \
                            'o' in [field[1][3]] and 'o' in [field[2][3]] and 'o' in [field[3][3]] or \
                            'o' in [field[1][1]] and 'o' in [field[2][2]] and 'o' in [field[3][3]] or \
                            'o' in [field[3][1]] and 'o' in [field[2][2]] and 'o' in [field[1][3]]:
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
