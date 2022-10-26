import random
import re
from typing import *


class Ship_1:
    def __init__(self, args: Tuple[Tuple, Tuple, Tuple, Tuple]):
        self.coord = args


class Ship_2:
    def __init__(self, args: Tuple[Tuple, Tuple, Tuple, Tuple]):
        self.coord = args
        
class Ship_3:
    def __init__(self, args: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]):
        self.coord = args


class Validator:
    def __init__(self, ship_1: Ship_1, ship_2: Ship_2, ship_3: Ship_3):
        print('   |', *[f' {i} |' for i in range(1, 7)], sep='')
        [print(''.join(j)) for i in range(1, 7) for j in [[str(i), '  | O |', ' O |', ' O |', ' O |', ' O |', ' O |']]]
        self.coord = []
        for _ in [*ship_1.coord, *ship_2.coord, *ship_3.coord]:
            self.coord.append(_)
        
        self.neighboring_cells = []
        for it in ship_1.coord:
            self.neighboring_cells.extend([(it[0], it[1] - 1), (it[0] - 1, it[1] - 1),
                                           (it[0] - 1, it[1]), (it[0] + 1, it[1] - 1),
                                           (it[0] + 1, it[1]), (it[0] + 1, it[1] + 1),
                                           (it[0] - 1, it[1] + 1), (it[0], it[1] + 1)
                                           ])
        if ship_2.coord[0][0] == ship_2.coord[1][0]:
            self.neighboring_cells.extend([(ship_2.coord[0][0], ship_2.coord[0][1] - 1), (ship_2.coord[0][0] - 1,
                                                                                          ship_2.coord[0][1] - 1),
                                           (ship_2.coord[0][0] - 1, ship_2.coord[0][1]), (ship_2.coord[0][0] + 1,
                                                                                          ship_2.coord[0][1] - 1),
                                           (ship_2.coord[0][0] + 1, ship_2.coord[0][1]),
                                           (ship_2.coord[1][0] - 1, ship_2.coord[1][1]),
                                           (ship_2.coord[1][0] - 1, ship_2.coord[1][1] + 1),
                                           (ship_2.coord[1][0], ship_2.coord[1][1] + 1),
                                           (ship_2.coord[1][0] + 1, ship_2.coord[1][1] + 1), (ship_2.coord[1][0] + 1,
                                                                                              ship_2.coord[1][1])
                                           ])
        if ship_2.coord[0][1] == ship_2.coord[1][1]:
            self.neighboring_cells.extend([(ship_2.coord[0][0], ship_2.coord[0][1] - 1), (ship_2.coord[0][0] - 1,
                                                                                          ship_2.coord[0][1] - 1),
                                           (ship_2.coord[0][0] - 1, ship_2.coord[0][1]), (ship_2.coord[0][0] - 1,
                                                                                          ship_2.coord[1][1] + 1),
                                           (ship_2.coord[0][0], ship_2.coord[0][1] + 1),
                                           (ship_2.coord[1][0], ship_2.coord[1][1] - 1), (ship_2.coord[1][0] + 1,
                                                                                          ship_2.coord[1][1] - 1),
                                           (ship_2.coord[1][0] + 1, ship_2.coord[1][1]), (ship_2.coord[1][0] + 1,
                                                                                          ship_2.coord[1][1] + 1),
                                           (ship_2.coord[1][0], ship_2.coord[1][1] + 1)
                                           ])
        if ship_2.coord[2][0] == ship_2.coord[3][0]:
            self.neighboring_cells.extend([(ship_2.coord[2][0], ship_2.coord[2][1] - 1), (ship_2.coord[2][0] - 1,
                                                                                          ship_2.coord[2][1] - 1),
                                           (ship_2.coord[2][0] - 1, ship_2.coord[2][1]), (ship_2.coord[2][0] + 1,
                                                                                          ship_2.coord[2][1] - 1),
                                           (ship_2.coord[2][0] + 1, ship_2.coord[2][1]),
                                           (ship_2.coord[3][0] - 1, ship_2.coord[3][1]),
                                           (ship_2.coord[3][0] - 1, ship_2.coord[3][1] + 1), (ship_2.coord[3][0],
                                                                                              ship_2.coord[3][1] + 1),
                                           (ship_2.coord[3][0] + 1, ship_2.coord[3][1] + 1), (ship_2.coord[3][0] +
                                                                                              1,
                                                                                              ship_2.coord[3][1])
                                           ])
        if ship_2.coord[2][1] == ship_2.coord[3][1]:
            self.neighboring_cells.extend([(ship_2.coord[2][0], ship_2.coord[2][1] - 1), (ship_2.coord[2][0] - 1,
                                                                                          ship_2.coord[2][1] - 1),
                                           (ship_2.coord[2][0] - 1, ship_2.coord[2][1]),
                                           (ship_2.coord[2][0] - 1, ship_2.coord[2][1] + 1),
                                           (ship_2.coord[2][0], ship_2.coord[2][1] + 1),
                                           (ship_2.coord[3][0], ship_2.coord[2][1] - 1), (ship_2.coord[3][0] + 1,
                                                                                          ship_2.coord[3][1] - 1),
                                           (ship_2.coord[3][0] + 1, ship_2.coord[3][1]), (ship_2.coord[3][0] + 1,
                                                                                          ship_2.coord[3][1] + 1),
                                           (ship_2.coord[3][0], ship_2.coord[3][1] + 1)
                                           ])
        if ship_3.coord[0][0] == ship_3.coord[1][0]:
            self.neighboring_cells.extend([(ship_3.coord[0][0], ship_3.coord[0][1] - 1), (ship_3.coord[0][0] - 1,
                                                                                          ship_3.coord[0][1] - 1),
                                           (ship_3.coord[0][0] - 1, ship_3.coord[0][1]), (ship_3.coord[0][0] + 1,
                                                                                          ship_3.coord[0][1] - 1),
                                           (ship_3.coord[0][0] + 1, ship_3.coord[0][1]), (ship_3.coord[0][0] + 1,
                                                                                          ship_3.coord[0][1] + 1),
                                           (ship_3.coord[0][0] - 1, ship_3.coord[0][1] + 1), (ship_3.coord[2][0] - 1,
                                                                                              ship_3.coord[2][1]),
                                           (ship_3.coord[2][0] - 1, ship_3.coord[2][1] + 1), (ship_3.coord[2][0],
                                                                                              ship_3.coord[2][1] + 1),
                                           (ship_3.coord[2][0] + 1, ship_3.coord[2][1] + 1), (ship_3.coord[2][0] + 1,
                                                                                              ship_3.coord[2][1])])
        
        if ship_3.coord[1][1] == ship_3.coord[2][1]:
            self.neighboring_cells.extend([(ship_3.coord[0][0], ship_3.coord[0][1] - 1), (ship_3.coord[0][0] - 1,
                                                                                          ship_3.coord[0][1] - 1),
                                           (ship_3.coord[0][0] - 1, ship_3.coord[0][1]),
                                           (ship_3.coord[0][0] + 1, ship_3.coord[0][1] - 1), (ship_3.coord[0][0] - 1,
                                                                                              ship_3.coord[0][1] + 1),
                                           (ship_3.coord[0][0], ship_3.coord[0][1] + 1),
                                           (ship_3.coord[0][0] + 1, ship_3.coord[0][1] + 1),
                                           (ship_3.coord[2][0], ship_3.coord[2][1] - 1), (ship_3.coord[2][0] + 1,
                                                                                          ship_3.coord[2][1] - 1),
                                           (ship_3.coord[2][0] + 1, ship_3.coord[2][1]),
                                           (ship_3.coord[2][0] + 1, ship_3.coord[2][1] + 1), (ship_3.coord[2][0],
                                                                                              ship_3.coord[2][1] + 1)])
        print('\n')
        print(self.coord, end='\n\n')
        print(self.neighboring_cells)
        print('\n')
        for i in self.coord:
            for j in self.neighboring_cells:
                if i == j:
                    print(f'{j} Не пойдёт - между кораблями должно быть более 1 клетки. Введи снова\n')
                    exit()
                    
class CompLayout:
    @classmethod
    def init(cls):
        
        _user_table = {i: ['   |'] * 7 for i in range(1, 7)}
        
        ship_1 = []
        around_cells = []
        all_points = {(i, j) for i in range(1, 7) for j in range(1, 7)}
        ship_1.extend([random.choice(list(all_points))])
        around_cells.extend([ship_1[0], (ship_1[0][0], ship_1[0][1] - 1), (ship_1[0][0] - 1, ship_1[0][1] - 1),
                             (ship_1[0][0] - 1, ship_1[0][1]), (ship_1[0][0] + 1, ship_1[0][1] - 1),
                             (ship_1[0][0] + 1, ship_1[0][1]), (ship_1[0][0] + 1, ship_1[0][1] + 1),
                             (ship_1[0][0] - 1, ship_1[0][1] + 1), (ship_1[0][0], ship_1[0][1] + 1)
                             ])
        
        all_points = all_points.difference(around_cells)
        for i in range(1, 4):
            ship_1.extend([random.choice(list(all_points))])
            all_points.discard(ship_1[i])
            around_cells.extend([(ship_1[i][0], ship_1[i][1] - 1), (ship_1[i][0] - 1, ship_1[i][1] - 1),
                                 (ship_1[i][0] - 1, ship_1[i][1]), (ship_1[i][0] + 1, ship_1[i][1] - 1),
                                 (ship_1[i][0] + 1, ship_1[i][1]), (ship_1[i][0] + 1, ship_1[i][1] + 1),
                                 (ship_1[i][0] - 1, ship_1[i][1] + 1), (ship_1[i][0], ship_1[i][1] + 1)
                                 ])
            all_points = all_points.difference(around_cells)

        ship_3 = []
        all_points_list = list(all_points)
        print(f'до цикла трёхпалубного {all_points_list}')
        count = 0
        for item in range(len(all_points) - 1):
            ship_3.append(all_points_list[item])
            for subitem in all_points_list[item + 1:]:
                if all_points_list[item][1] == subitem[1] and all_points_list[item][0] - subitem[0] in [1, -1]:
                    ship_3.append(subitem)
                    if len(ship_3) == 3:
                        break
            if len(ship_3) == 3:
                break
            else:
                ship_3.clear()
                continue

        if len(ship_3) == 0:
            count = 1
            for item in range(len(all_points) - 1):
                ship_3.append(all_points_list[item])
                for subitem in all_points_list[item + 1:]:
                    if all_points_list[item][0] == subitem[0] and all_points_list[item][1] - subitem[1] in [1, -1]:
                        ship_3.append(subitem)
                        if len(ship_3) == 3:
                            break
                if len(ship_3) == 3:
                    break
                else:
                    ship_3.clear()
                    continue

        print(f'before {len(all_points)}--{all_points=}')
        all_points = set(all_points_list).difference(ship_3)
        print(f'after {len(all_points)} {all_points=}')
        ship_3.sort()

        ship_2 = []
        all_points_list = list(all_points)
        for item in range(len(all_points_list) - 1):
            ship_2.append(all_points_list[item])
            for subitem in all_points_list[item + 1:]:
                if all_points_list[item][0] == subitem[0] and all_points_list[item][1] - subitem[1] in [1, -1]:
                    ship_2.append(subitem)
                    break
            if len(ship_2) == 2:
                break
            else:
                ship_2.clear()
                continue

        around_cells = [*ship_2, (ship_2[0][0], ship_2[0][1] - 1), (ship_2[0][0] - 1, ship_2[0][1] - 1),
                        (ship_2[0][0] - 1,
                         ship_2[0][1]),
                        (ship_2[0][0] + 1, ship_2[0][1] - 1), (ship_2[0][0] + 1, ship_2[0][1]),
                        (ship_2[1][0] - 1, ship_2[1][1]),
                        (ship_2[1][0] - 1, ship_2[1][1] + 1), (ship_2[1][0], ship_2[1][1] + 1),
                        (ship_2[1][0] + 1, ship_2[1][1] + 1),
                        (ship_2[1][0] + 1, ship_2[1][1])]
        all_points_list = list(set(all_points_list).difference(around_cells))

        around_cells = [*ship_2, (ship_2[0][0], ship_2[0][1] - 1), (ship_2[0][0] - 1, ship_2[0][1] - 1),
                        (ship_2[0][0] - 1,
                         ship_2[0][1]),
                        (ship_2[0][0] - 1, ship_2[1][1] + 1), (ship_2[0][0], ship_2[0][1] + 1),
                        (ship_2[1][0], ship_2[1][1] - 1),
                        (ship_2[1][0] + 1, ship_2[1][1] - 1), (ship_2[1][0] + 1, ship_2[1][1]),
                        (ship_2[1][0] + 1, ship_2[1][1] + 1),
                        (ship_2[1][0], ship_2[1][1] + 1)]

        print(f'count around {count}---{around_cells} ')

        all_points_list = list(set(all_points_list).difference(around_cells))

        for item2 in range(len(all_points_list) - 1):
            ship_2.append(all_points_list[item2])
            for subitem in all_points_list[item2 + 1:]:
                if all_points_list[item2][1] == subitem[1] and all_points_list[item2][0] - subitem[0] in [1, -1] or \
                        all_points_list[item2][0] == subitem[0] and all_points_list[item2][1] - subitem[1] in [1, -1]:
                    ship_2.append(subitem)
                    break
            if len(ship_2) == 4:
                break
            else:
                ship_2.clear()
                continue
        print(f'{ship_3=}')
        print(f'{ship_2=}')
        
        return [*ship_1, *ship_3, *ship_2]
        
class Board:
    _user_table = {i: ['   |'] * 7 for i in range(1, 7)}
    _comp_table = {i: ['   |'] * 7 for i in range(1, 7)}
    
    def __init__(self, ships: Validator):
        self.comp_cells = [(4, 1), (4, 2), (4, 3), (5, 6), (6, 6), (1, 3), (2, 3),
                                                           (3, 6), (2, 1), (6, 2), (1, 1)]
        self.user_cells = ships.coord
        self.comp_cells = CompLayout.init()
        for p in self.user_cells:
            self._user_table[p[0]][p[1]] = ' K |'
        for c in self.comp_cells:
            self._comp_table[c[0]][c[1]] = ' K |'
        self._display_user_table()    
        print('\nКорабли расставлены нормально. Начинаем игру')
            
    
    def display_all(self):
        print('\n')
        print('   |', *[f' {i} |' for i in self._user_table], sep='')
        [print(str(i) + '  |' + ''.join(self._user_table[i][1:])) for i in self._user_table]
        print('\n')
        print('   |', *[f' {i} |' for i in self._comp_table], sep='')
        [print(str(i) + '  |' + ''.join(self._comp_table[i][1:])) for i in self._comp_table]
    
    def _display_comp_table(self):
        print('   |', *[f' {i} |' for i in self._comp_table], sep='')
        [print(str(i) + '  |' + ''.join(self._comp_table[i][1:])) for i in self._comp_table]
    
    def _display_user_table(self):
        print('   |', *[f' {i} |' for i in self._user_table], sep='')
        [print(str(i) + '  |' + ''.join(self._user_table[i][1:])) for i in self._user_table]
    
    def game(self):
       
        past_user_turns = []
        past_comp_turns = []
        user_hits = 0
        comp_hits = 0
        while True:
            try:
                x = input('\nВаш ход: две цифры через пробел ')
                if re.match('^[1-6]\s[1-6]$', x):
                    x = x.split(' ')
                    if (int(x[0]), int(x[1])) in self.comp_cells and (int(x[0]), int(x[1])) not in [
                        *past_user_turns]:
                        self._comp_table[int(x[0])][int(x[1])] = ' X |'
                        past_user_turns.append((int(x[0]), int(x[1])))
                        user_hits += 1
                        print('\nПоле компьютера\n')
                        self._display_comp_table()
                        print(f'\nПопадание игрока: {x}')
                        
                    elif (int(x[0]), int(x[1])) not in [*self.comp_cells,
                                                        *past_user_turns]:
                        self._comp_table[int(x[0])][int(x[1])] = ' T |'
                        print('\nПоле компьютера\n')
                        self._display_comp_table()
                        print(f'\nВы промахнулись: {(int(x[0]), int(x[1]))} ')
                        past_user_turns.append((int(x[0]), int(x[1])))
                    else:
                        raise Exception
                else:
                    raise Exception
            except Exception:
                print('\nНеправильный ход. Попробуй ещё\n')
                self._display_comp_table()
                continue
            
            else:
                while True:
                    comp_turn = (random.randint(1, 6), random.randint(1, 6))
                    if comp_turn in self.user_cells and comp_turn not in [*past_comp_turns]:
                        self._user_table[comp_turn[0]][comp_turn[1]] = ' X |'
                        print('\nПоле игрока\n')
                        self._display_user_table()
                        print(f'\nКомпьютер попал: {comp_turn}')
                        past_comp_turns.append(comp_turn)
                        comp_hits += 1
                        break
                    elif comp_turn not in [*self.user_cells, *past_comp_turns]:
                        self._user_table[comp_turn[0]][comp_turn[1]] = ' T |'
                        past_comp_turns.append(comp_turn)
                        print('\nПоле игрока\n')
                        self._display_user_table()
                        print(f'\nКомпьютер промахнулся: {comp_turn}')
                        break
                    else:
                        continue
            if user_hits == 11:
                print('\nИгра окончена. Игрок выиграл')
                exit()
            elif comp_hits == 11:
                print('\nИгра окончена. Компьютер выиграл')
                exit()



if __name__ == '__main__':
        
    b = Board(Validator(Ship_1(((1, 1), (1, 3), (1, 5), (3, 1))), Ship_2(((3, 3), (4, 3), (3, 6), (4, 6))), 
                            Ship_3(((6, 2), (6, 3),(6, 4)))))
    b.game()
