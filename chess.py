from abc import ABC, abstractmethod

class Chess_desk:
    def __init__(self):
        self.desk = [[' ' for _ in range(8)] for _ in range(8)]
        for i in range(8):
            self.desk[i][1] = Pawn(self.desk, 'black', i, 1)
            self.desk[i][6] = Pawn(self.desk, 'white', i, 6)

        self.desk[0][0], self.desk[7][0] = Rook(self.desk, 'black', 0, 0), Rook(self.desk, 'black', 7, 0)
        self.desk[0][7], self.desk[7][7] = Rook(self.desk, 'white', 0, 7), Rook(self.desk, 'white', 7, 7)

        self.desk[1][0], self.desk[6][0] = Horse(self.desk, 'black', 1, 0), Horse(self.desk, 'black', 6, 0)
        self.desk[1][7], self.desk[6][7] = Horse(self.desk, 'white', 1, 7), Horse(self.desk, 'white', 6, 7)

        self.desk[2][0], self.desk[5][0] = Elephant(self.desk, 'black', 2, 0), Elephant(self.desk, 'black', 5, 0)
        self.desk[2][7], self.desk[5][7] = Elephant(self.desk, 'white', 2, 7), Elephant(self.desk, 'white', 5, 7)

        self.desk[3][0], self.desk[4][7] = King(self.desk, 'black', 3, 0), King(self.desk, 'white', 4, 7)
        self.desk[4][0], self.desk[3][7] = Queen(self.desk, 'white', 4, 0), Queen(self.desk, 'white', 3, 7)


    def move_figure(self, current_pos_x, current_pos_y, new_pos_x, new_pos_y): #переместить фигуру
        if self.desk[current_pos_x][current_pos_y] != ' ' and [new_pos_x, new_pos_y] in self.desk[current_pos_x][current_pos_y].moves_check():
            self.desk[new_pos_x][new_pos_y] = self.desk[current_pos_x][current_pos_y]
            self.desk[current_pos_x][current_pos_y] = ' '
            self.desk[new_pos_x][new_pos_y].desk = self.desk
            return True
        return False

    def __str__(self): #вывести шахматную доску
        str_return = ''
        for i in range(8):
            for j in range(8):
                if self.desk[j][i] == ' ':
                    str_return += str(j) + str(i)
                else:
                    str_return += str(self.desk[j][i])
                str_return += ' '
            str_return += '\n'

        return str_return

class Figure(ABC):

    def __init__(self, desk, color, pos_x, pos_y):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.desk = desk

    @abstractmethod
    def moves_check(self): #вывести список возможных ходов
        pass

    @abstractmethod
    def __str__(self):
        if self.color == 'black':
            return 'Ч'
        else:
            return 'Б'

class Pawn(Figure):

    def __init__(self, desk, color, pos_x, pos_y):
        super().__init__(desk, color, pos_x, pos_y)
        self.moves_count = 0

    def moves_check(self):
        moves_list = []
        if self.color == 'white':
            first_term = -1
        else:
            first_term = 1

        if self.desk[self.pos_x][self.pos_y+first_term] == ' ':
            moves_list.append([self.pos_x, self.pos_y+first_term])

            if self.moves_count == 0 and self.desk[self.pos_x][self.pos_y+(first_term * 2)] == ' ':
                moves_list.append([self.pos_x, self.pos_y + (first_term * 2)])
                self.moves_count += 1

        for i in range(-1, 2, 2):
            if self.desk[self.pos_x+i][self.pos_y + first_term] != ' ' and self.desk[self.pos_x+i][self.pos_y + first_term].color != self.color:
                moves_list.append([self.pos_x+i, self.pos_y+first_term])

        return moves_list

    def __str__(self):
        return Figure.__str__(self) + 'П'

class Rook(Figure):

    def moves_check(self):
        moves_list = []

        for i in range(self.pos_x-1, -1, -1):
            if self.desk[i][self.pos_y] == ' ':
                moves_list.append([i, self.pos_y])

            elif self.desk[i][self.pos_y].color != self.color:
                moves_list.append([i, self.pos_y])
                break

            else:
                break

        for i in range(self.pos_x+1, 8):
            if self.desk[i][self.pos_y] == ' ':
                moves_list.append([i, self.pos_y])

            elif self.desk[i][self.pos_y].color != self.color:
                moves_list.append([i, self.pos_y])
                break

            else:
                break

        for i in range(self.pos_y-1, -1, -1):
            if self.desk[self.pos_x][i] == ' ':
                moves_list.append([self.pos_x, i])

            elif self.desk[self.pos_x][i].color != self.color:
                moves_list.append([self.pos_x, i])
                break

            else:
                break

        for i in range(self.pos_y+1, 8):
            if self.desk[self.pos_x][i] == ' ':
                moves_list.append([self.pos_x, i])

            elif self.desk[self.pos_x][i].color != self.color:
                moves_list.append([self.pos_x, i])
                break

            else:
                break

        return moves_list

    def __str__(self):
        return Figure.__str__(self) + 'Л'

class Horse(Figure):

    def moves_check(self):
        moves_list = []
        for i in range(-2, 3):
            if i == 0:
                continue
            for j in range(-2, 3):
                if j == 0 or abs(i) == abs(j):
                    continue
                try:
                    if self.desk[self.pos_x+i][self.pos_y+j] == ' ' or self.desk[self.pos_x+i][self.pos_y+j].color != self.color:
                        moves_list.append([self.pos_x+i, self.pos_y+j])
                except IndexError:
                    pass

        return moves_list

    def __str__(self):
        return Figure.__str__(self) + 'К'

class Elephant(Figure):

    def moves_check(self):
        moves_list = []
        i = 1
        while self.pos_x - i > -1 and self.pos_y - i > -1:

            if self.desk[self.pos_x-i][self.pos_y-i] == ' ':
                moves_list.append([self.pos_x-i, self.pos_y-i])

            elif self.desk[self.pos_x-i][self.pos_y-i].color != self.color:
                moves_list.append([self.pos_x-i, self.pos_y-i])
                break

            else:
                break
            i += 1

        i = 1
        while self.pos_x - i > -1 and self.pos_y + i < 8:

            if self.desk[self.pos_x - i][self.pos_y + i] == ' ':
                moves_list.append([self.pos_x - i, self.pos_y + i])

            elif self.desk[self.pos_x - i][self.pos_y + i].color != self.color:
                moves_list.append([self.pos_x - i, self.pos_y + i])
                break

            else:
                break
            i += 1

        i = 1
        while self.pos_x + i < 8 and self.pos_y - i > -1:

            if self.desk[self.pos_x + i][self.pos_y - i] == ' ':
                moves_list.append([self.pos_x + i, self.pos_y - i])

            elif self.desk[self.pos_x + i][self.pos_y - i].color != self.color:
                moves_list.append([self.pos_x + i, self.pos_y - i])
                break

            else:
                break

            i += 1

        i = 1
        while self.pos_x + i < 8 and self.pos_y + i < 8:

            if self.desk[self.pos_x + i][self.pos_y + i] == ' ':
                moves_list.append([self.pos_x + i, self.pos_y + i])

            elif self.desk[self.pos_x + i][self.pos_y + i].color != self.color:
                moves_list.append([self.pos_x + i, self.pos_y + i])
                break

            else:
                break

            i += 1

        return moves_list

    def __str__(self):
        return Figure.__str__(self) + 'С'

class Queen(Figure):

    def moves_check(self):
        return Elephant.moves_check(self) + Rook.moves_check(self)

    def __str__(self):
        return Figure.__str__(self) + 'Q'

class King(Figure):

    def moves_check(self):
        queen_moves_list = Queen.moves_check(self)
        moves_list = []
        for moves in queen_moves_list:
            if abs(self.pos_x - moves[0]) <= 1 and abs(self.pos_y - moves[1]) <= 1:
                moves_list.append(moves)

        return moves_list

    def __str__(self):
        return Figure.__str__(self) + 'К'

test = Chess_desk()
print(test)


