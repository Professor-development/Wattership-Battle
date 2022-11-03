MAX_X = 6
MAX_Y = 6
MAX_SHIP_TYPE = 3


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def __str__(self):
        return f'Dot({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, x, y, rotate, ship_type):
        self.x = x
        self.y = y
        self.rotate = rotate
        self.ship_type = ship_type
        self.own_coordinate = []
        for i in range(0, ship_type):
            if rotate == 0:
                self.own_coordinate.append(Dot(x, y + i))
            if rotate == 1:
                self.own_coordinate.append(Dot(x + i, y))


class Board:
    def __init__(self, hide=False):
        self.hide = hide
        self.canvas = [['O' for _ in range(MAX_X)] for _ in range(MAX_Y)]

    def draw(self):
        temp_str = ' '
        for i in range(1, MAX_X+1):
            temp_str += f' | {i}'
        print(temp_str)
        for i in range(1, MAX_X+1):
            temp_str = ''
            for j in range(0, MAX_Y+1):
                if j == 0 and i < 10:
                    temp_str += f'{i}'
                else:
                    temp_str += f' | {self.canvas[i-1][j-1]}'
            print(temp_str)


d = Dot(1, 2)
a = Dot(2, 3)
c = Dot(4, 5)
print([d, a, c])