class Figure:
    color = 'white' or 'black'

    coordinate_place: list = [4, 4]
    first_coordinate = range(0, 8)
    second_coorinate = range(0, 8)

    def set_color(self):
        if self.color == 'white':
            return print('black')
        else:
            return print('white')

    def walk_check(self, one: int, two: int):
        if one not in self.first_coordinate or two not in self.second_coorinate:
            return print('Ход не возможен, фигура окажеться за доской')
        else:
            return print('Ход возможен')
        raise NotImplementedError

    def walk_figure(self, one: int, two: int):
        if one not in self.first_coordinate or two not in self.second_coorinate:
            return print('Ход не возможен, фигура окажеться за доской')
        elif one in self.first_coordinate or two in self.second_coorinate:
            self.coordinate_place.clear(),
            self.coordinate_place.insert(0, one), self.coordinate_place.insert(1, two)
            return print(f'Ход возможен, фигура перемещена на клетку {one} по гирозонтали {two} по вертикали')

    def my_coordinate(self):
        print(f'Вы находитесь в клетке {self.coordinate_place[0]} по горизонтали,\
{self.coordinate_place[1]} по вертикали')


class King(Figure):
    def king_walk(self, one: int, two: int):
        if abs(one - self.coordinate_place[0]) <= 1 and \
                abs(two - self.coordinate_place[1]) <= 1:
            self.walk_figure(one, two)
        else:
            return print('Король так не ходит')


class Rook(Figure):
    def rook_walk(self, one: int, two: int):
        if one == self.coordinate_place[0] and self.coordinate_place[1] in self.first_coordinate\
                or two == self.coordinate_place[1] and self.coordinate_place[0]\
                in self.first_coordinate:
            self.walk_figure(one, two)
        else:
            return print('Ладья так не ходит')


class Officer(Figure):
    def officer_walk(self, one: int, two: int):
        if abs(one - self.coordinate_place[0]) == abs(two - self.coordinate_place[1]):
            super().walk_figure(one, two)
        else:
            return print('Офицер так не ходит')


class Queen(Figure):
    def queen_walk(self, one: int, two: int):
        if abs(one - self.coordinate_place[0]) == abs(two - self.coordinate_place[1]):
            self.walk_figure(one, two)
        if one == self.coordinate_place[0] and self.coordinate_place[1] in self.first_coordinate \
                or two == self.coordinate_place[1] and self.coordinate_place[0] in self.first_coordinate:
            self.walk_figure(one, two)
        else:
            return print("Королева так не ходит")


class Pawn(Figure):
    def pawn_walk(self, one, two, color):
        if color == 'white' and one == self.coordinate_place[0] and two == two - self.coordinate_place[1] == 1:
            self.walk_figure(one, two)
        if color == 'black' and one == self.coordinate_place[0] and two == two - self.coordinate_place[1] == -1:
            self.walk_figure(one, two)
        else:
            return print(f'Пешка {color} так не ходит')


queen = Queen()
king = King()
rook = Rook()
officer = Officer()
pawn = Pawn()


def check_all_move(one, two):
    can_move = []
    if officer.walk_figure(one, two):
        can_move.append('King')
    else:
        print('NO')
    return print(can_move)


officer.my_coordinate()
check_all_move(5, 7)
pawn.my_coordinate()
pawn.pawn_walk(6, 7, 'white')