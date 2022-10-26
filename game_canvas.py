import random

from ship_class import Ship
from ship_class import CoordinateDict


class Canvas:

    def __init__(self, auto):
        self._ship_list = CoordinateDict()
        self._canvas = self.base_canvas()
        if auto:
            self.auto_ships_placement()
        self._number_of_ships = [0, 0, 0]

    @property
    def ship_list(self):
        return self._ship_list.get_values()

    @property
    def number_of_ships(self):
        return self._number_of_ships

    @staticmethod
    def base_canvas():
        output_canvas = [[" ", '1', '2', '3', '4', '5', '6', '7']]
        for i in range(7):
            temp_list = list()
            for j in range(8):
                if j == 0:
                    temp_list.append(str(i + 1))
                else:
                    temp_list.append("O")
            output_canvas.append(temp_list)
        return output_canvas

    def self_cleaner(self):
        self._number_of_ships = [0, 0, 0]
        self._ship_list.clear()
        for i in range(1, 8):
            for j in range(1, 8):
                self._canvas[i][j] = "O"

    def add_ship(self, ship: Ship):
        own_position = ship.get_own_position()
        if self.check_add_ship(ship) == 'access':
            self.number_of_ships[ship.ship_type-1] += 1
            for i in own_position:
                self._ship_list.update(i[1], i[0], 1)
            for row in own_position:
                self._canvas[row[0]][row[1]] = "*"

    def check_add_ship(self, ship: Ship):
        if ship.ship_type < 1 or ship.ship_type > 3:
            return 'Не существует коробля такого типа'
        elif ship.rotate > 2 or ship.rotate < 1:
            return 'Недопустимое значение поворота коробля'
        elif ship.x == 5 and ship.ship_type == 3 and ship.rotate == 1:
            return 'Корабль выходит за границы поля'
        elif ship.x == 6 and ship.ship_type != 1 and ship.rotate == 1:
            return 'Корабль выходит за границы поля'
        elif ship.y == 5 and ship.ship_type == 3 and ship.rotate == 2:
            return 'Корабль выходит за границы поля'
        elif ship.y == 6 and ship.ship_type != 1 and ship.rotate == 2:
            return 'Корабль выходит за границы поля'
        elif self.number_of_ships[2] >= 1 and ship.ship_type == 3:
            return 'Превышено максимальное количество кораблей 3 типа'
        elif self.number_of_ships[1] >= 2 and ship.ship_type == 2:
            return 'Превышено максимальное количество кораблей 2 типа'
        elif self.number_of_ships[0] >= 4 and ship.ship_type == 1:
            return 'Превышено максимальное количество кораблей 1 типа'
        own_position = ship.get_own_position()
        own_len = len(own_position)
        if own_position[0][0] < 1 or own_position[0][1] < 1 or own_position[own_len-1][0] > 6 or own_position[own_len-1][1] > 6:
            return 'Корабль выходит за границы поля'
        for i in range(own_position[0][0]-1, own_position[own_len-1][0]+2):
            for j in range(own_position[0][1]-1, own_position[own_len-1][1]+2):
                if self._canvas[i][j] == "*":
                    return 'Корабль близко располжен по отношению к другому кораблю'
        return 'access'

    def shot(self, x, y):
        if self._canvas[y][x] == "*":
            self._canvas[y][x] = "X"
            self._ship_list.change_value(self._ship_list.find(x, y), 0)
        else:
            self._canvas[y][x] = "T"

    def defeat(self):
        for i in range(self._ship_list.length()):
            if self._ship_list.get_value(i)[1] != 0:
                return False
        return True

    def auto_ships_placement(self):
        a = 0
        while True:
            counter = 0
            counter_all = 0
            self.self_cleaner()
            for i in range(300):
                x = random.randrange(1, 7)
                y = random.randrange(1, 7)
                r1 = random.randrange(1, 3)
                temp_ship1 = Ship(x, y, 3, r1)
                if self.check_add_ship(temp_ship1) == 'access':
                    self.add_ship(temp_ship1)
                    counter += 1
                    counter_all += 1
                if counter >= 1:
                    break
            counter = 0
            for i in range(300):
                x1 = random.randrange(1, 7)
                y1 = random.randrange(1, 7)
                r1 = random.randrange(1, 3)
                temp_ship2 = Ship(x1, y1, 2, r1)
                if self.check_add_ship(temp_ship2) == 'access':
                    self.add_ship(temp_ship2)
                    counter += 1
                    counter_all += 1
                if counter >= 2:
                    break
            counter = 0
            for i in range(300):
                x1 = random.randrange(1, 7)
                y1 = random.randrange(1, 7)
                temp_ship3 = Ship(x1, y1, 1)
                if self.check_add_ship(temp_ship3) == 'access':
                    self.add_ship(temp_ship3)
                    counter += 1
                    counter_all += 1
                if counter >= 4:
                    break
            a += 1
            if counter_all >= 7:
                break


class ComputerCanvas(Canvas):

    def __init__(self, auto=True):
        super().__init__(auto)
        self._computer_shoots_base = CoordinateDict()
        self.base_coordinate_base(self._computer_shoots_base)
        self.auto_ships_placement()

    @staticmethod
    def base_coordinate_base(coordinate_base):
        for i in range(1, 7):
            for j in range(1, 7):
                coordinate_base.update(i, j, 0)

    @property
    def computer_shoots_base(self):
        return self._computer_shoots_base.get_values()

    def draw_visible(self):
        for i in range(7):
            temp_row = ""
            for j in range(7):
                temp_row += self._canvas[i][j]
                temp_row += " | "
            print(temp_row)

    def draw_canvas(self):
        for i in range(7):
            temp_row = ""
            for j in range(7):
                if self._canvas[i][j] == "T":
                    temp_row += "T"
                elif self._canvas[i][j] == "X":
                    temp_row += "X"
                elif self._canvas[i][j] == "*":
                    temp_row += "O"
                else:
                    temp_row += self._canvas[i][j]
                temp_row += " | "
            print(temp_row)

    def computer_shoot(self):
        element = random.randrange(self._computer_shoots_base.length())
        temp_coordinate = self._computer_shoots_base.get_key(element)
        self._computer_shoots_base.del_element(element)
        return temp_coordinate


class PlayerCanvas(Canvas):

    def __init__(self, auto=False):
        super().__init__(auto)

    def draw_canvas(self):
        for i in range(7):
            temp_row = ""
            for j in range(7):
                temp_row += self._canvas[i][j]
                temp_row += " | "
            print(temp_row)
