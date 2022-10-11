def tic_tac_toe():
    '''
    Классическая игра в крестики-нолики. Игроки по очереди вводят координаты ходов
     
    '''
    import re
    
    field = [
             [' ', '1',  '2', '3'], 
             ['1', ' ', ' ', ' '],
             ['2', ' ', ' ', ' '],
             ['3', ' ', ' ', ' ']
    ]
    while True:
        while True:
                
            x = input('Ход крестика. Введите через один пробел координаты клетки для крестика (сначала координата по '
                      'вертикали, '
                      'затем по горизонтали.): ')
            
            if re.match(r'^[1-3]\s[1-3]$', x):
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
                break
            else: print('Неправильно введены координаты - попробуйте снова\n')
    
        while True:
    
            x = input('Ход нолика. Введите через один пробел координаты клетки для нолика (сначала координата по '
                      'вертикали, '
                      'затем по горизонтали): ')
        
            if re.match(r'^[1-3]\s[1-3]$', x):
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
                break
            else:
                print('Неправильно введены координаты - попробуйте снова\n')

tic_tac_toe()

