SIZE = 6
MAX_SHIP_TYPE = 3


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, bow: Dot, rotate, ship_type):
        self.bow = bow
        self.rotate = rotate
        self.ship_type = ship_type
        self.lives = ship_type

    @property
    def dots(self):
        ship_dots = [self.bow]
        if self.rotate == 0:
            for i in range(1, self.ship_type):
                ship_dots.append(Dot(self.bow.x, self.bow.y + i))
        elif self.rotate == 1:
            for i in range(1, self.ship_type):
                ship_dots.append(Dot(self.bow.x + i, self.bow.y))
        return ship_dots

    def shoten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=SIZE):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [["O"] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        res = ''
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"
        if self.hid:
            res = res.replace('■', 'O')
        return res

    def out(self, d: Dot):
        return not ((0 < d.x <= self.size) and (0 < d.y <= self.size))

    def contour(self, ship: Ship):
        pass

    def add_ship(self, ship: Ship):
        if self.count >= 7:
            return "Достигнуто максимальное количество кораблей"


b = Board(False, SIZE)
s = Ship(Dot(1, 2), 1, 3)
print(*s.dots)
print(s.dots)
print(b)
