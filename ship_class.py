class Ship:

    def __init__(self, x, y, ship_type, rotate=1):
        self._x = x
        self._y = y
        self._rotate = rotate
        self._ship_type = ship_type
        self._own_position = list()
        self.on_init_own_position()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if 1 <= value <= 6:
            self._x = value
        else:
            raise ValueError("Введенная координата находиться за пределами допустимых координат")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 1 <= value <= 6:
            self._y = value
        else:
            raise ValueError("Введенная координата находиться за пределами допустимых координат")

    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, value):
        if value == 1:
            self._rotate = 1
        elif value == 2:
            self._rotate = 2
        else:
            raise ValueError("Недопустимое положение поворота")

    @property
    def ship_type(self):
        return self._ship_type

    @ship_type.setter
    def ship_type(self, value):
        if 1 <= value <= 3:
            self._ship_type = value
        else:
            raise ValueError("Недопустимый номер коробля")

    def get_own_position(self):
        return self._own_position

    def on_init_own_position(self):
        if self.ship_type == 1:
            self._own_position = [[self.y, self.x]]
        elif self.ship_type == 2:
            if self.rotate == 1:
                self._own_position = [[self.y, self.x], [self.y, self.x + 1]]
            else:
                self._own_position = [[self.y, self.x], [self.y + 1, self.x]]
        elif self.ship_type == 3:
            if self.rotate == 1:
                self._own_position = [[self.y, self.x], [self.y, self.x + 1], [self.y, self.x + 2]]
            else:
                self._own_position = [[self.y, self.x], [self.y + 1, self.x], [self.y + 2, self.x]]


class CoordinateDict:

    def __init__(self):
        self._values = []

    def update(self, x, y, value=1):
        temp_app = [(x, y), value]
        self._values.append(temp_app)

    def find(self, x, y):
        for i in range(len(self._values)):
            if self._values[i][0][0] == x and self._values[i][0][1] == y:
                return int(i)
        return False

    def change_value(self, i, value):
        self._values[i][1] = value

    def get_value(self, i):
        return self._values[i]

    def get_values(self):
        return self._values

    def length(self):
        return len(self._values)

    def get_key(self, i):
        return self._values[i][0][0], self._values[i][0][1]

    def del_element(self, i):
        self._values.pop(i)

    def clear(self):
        self._values = []
