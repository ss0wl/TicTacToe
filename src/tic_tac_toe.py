"""
Класс TicTacToe описывает реализацию игры Крестики-нолики
"""

class TicTacToe():

    def __init__(self, player_symbol: str):
        
        # создаем нашу сетку
        self.field = []

        # заполняем её пустыми строками
        for i in range(9):
            self.field.append(" ") 

        if player_symbol == 'O' or player_symbol == 'X': 
            # объявляем символ игрока
            self.player_symbol = player_symbol
        else:
            self.player_symbol = " "
            raise ValueError("Вы создали инициализировали объект неизвестным символом!")

    def restart(self):
        """
        Функция, которая отвечает за перезапуск игры, очистку игрового поля
         
        """ 
        for i in range(9):
            self.field[i] = " "

    def draw_field(self):
        """
        Функция, которая выводит содержимое игрового поля на экран
        
        Пример вывода:
             A   B   C
        1    X ║   ║  
            ═══╬═══╬═══
        2      ║ O ║  
            ═══╬═══╬═══
        3      ║   ║ X 
        
        """
        
        delimeter = "      ═══╬═══╬═══"
        # координаты столбцов
        print("\n       A   B   C\n")
        
        # печатаем первую строку 
        first_row = "   1   " + self.field[0]
        first_row += " ║ " + self.field[1]
        first_row += " ║ " + self.field[2]
        print(first_row)

        # печатаем разделитель
        print(delimeter)

        # печатаем вторую строку
        second_row = "   2   " + self.field[3]
        second_row += " ║ " + self.field[4]
        second_row += " ║ " + self.field[5]
        print(second_row)

        # печатаем разделитель
        print(delimeter)

        # display third and last row 
        third_row = "   3   " + self.field[6]
        third_row += " ║ " + self.field[7]
        third_row += " ║ " + self.field[8]
        print(third_row, "\n") 

    def check_coord(self, field_coord: str):
        """
        Функция, которая проверяет координаты вида "1A" или "A1" на допустимые значения и возвращает True в случае, если координата существует и False в случае, если координата не существует 
        
        :param field_coord: координата в виде строки
        :return: True или False
        
        """
        allowed_char = ['A', 'B', 'C']
        allowed_num = [1, 2, 3]
        flag = False
        if len(field_coord) == 2:
            if field_coord[0].isdigit():
                for num in allowed_num:
                    if int(field_coord[0]) == num:
                        flag = True
                        break
                if field_coord[1].isalpha():
                    for ch in allowed_char:
                        if field_coord[1] == ch:
                            flag = flag ^ True
                            break
                else:
                    flag = True
            elif field_coord[1].isdigit():
                for num in allowed_num:
                    if int(field_coord[1]) == num:
                        flag = True
                        break
                if field_coord[0].isalpha():
                    for ch in allowed_char:
                        if field_coord[0] == ch:
                            flag = flag ^ True
                            break
                else:
                    flag = True
            else:
                flag = True
        else:
            flag = True
        
        if flag:
            return False
        else:
            return True                
                        
    def str_coord_to_int(self, field_coord: str):
        """
        Функция, которая получает координаты вида "1A" или "A1" и преобразует их в целое число 0..8
        
        :param field_coord: координата в виде строки
        :return: Целое число 0..8
        
        """
        if not self.check_coord(field_coord): return -1
        
        if field_coord[0].isdigit():
            field_coord = field_coord[1] + field_coord[0]
        
        col = field_coord[0]
        row = int(field_coord[1])
        
        symbols = {'A': 0, 'B': 1, 'C': 2}
        
        coord = 3 * (row - 1) + symbols[col]
        
        return coord
        
    def edit_field(self, field_coord: str):
        """
        Функция, которая изменяет значение клетки игрового поля
        
        :param field_coord: координата в виде строки
        :return: True, если операция была выполнена, False, если операция не выполнена
        
        """
        if not self.check_coord(field_coord):
            return False
        
        coord = self.str_coord_to_int(field_coord)

        if self.field[coord] == " ":
            self.field[coord] = self.player_symbol
            return True
        else:
            return False

    def update_field(self, other_field: list):
        """
        Функция, которая обновляет игровое поле игровым полем другого игрока
        
        :param other_field: игровое поле, которым дополняется наше поле
        
        """
        if len(other_field) != 9:
            raise ValueError("Вы передали в функцию игровое поле неверного размера!")
        for i in range(9):
            if self.field[i] != 'X' and self.field[i] != 'O':
                if other_field[i] != 'X' and other_field[i] != 'O' and other_field[i] != ' ':
                    raise TypeError("Вы передали в функцию игровое поле с неверными значениями!")
                self.field[i] = other_field[i]

    def is_win(self, player_symbol: str):
        """
        Функция, которая проверяет выиграл ли пользователь с определенным символом
        
        :param player_symbol: Может принимать значения 'X' или 'O' 
        :return: True, если игрок с символом, переданным в качестве аргумента, выиграл или False, если напротив, игрок с этим символом проиграл 
        
        """
        g = []
        for i in range(9):
            g.append(self.field[i])

        sym = player_symbol

        # проверяем первую строку 
        if g[0] == sym and g[1] == sym and g[2] == sym:
            return True

        # проверяем вторую строку
        elif g[3] == sym and g[4] == sym and g[5] == sym:
            return True
        
        # проверяем третью строку
        elif g[6] == sym and g[7] == sym and g[8] == sym:
            return True 

        # проверяем первый столбец
        elif g[0] == sym and g[3] == sym and g[6] == sym:
            return True 

        # проверяем второй столбец
        elif g[1] == sym and g[4] == sym and g[7] == sym:
            return True 

        # проверяем третий столбец
        elif g[2] == sym and g[5] == sym and g[8] == sym:
            return True

        # проверяем убывающую диагональ 
        elif g[2] == sym and g[4] == sym and g[6] == sym:
            return True 

        # проверяем возрастающую диагональ 
        elif g[0] == sym and g[4] == sym and g[8] == sym:
            return True 

        return False

    def is_full(self):
        """
        Функция, которая проверяет игровое поле на заполненность 
        
        :return: True, если ни один игрок не выиграл, но поле полностью заполнено, False, если какой-либо игрок победил, либо поле заполнено не полностью
        
        """
        num_blanks = 0
        for i in range(9):
                if self.field[i] == " ":
                    num_blanks += 1

        if self.is_win(self.player_symbol) == False and num_blanks == 0:
            return True
        else:
            return False
