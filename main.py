from ship_class import Ship
from ship_class import CoordinateDict
from game_canvas import PlayerCanvas
from game_canvas import ComputerCanvas


def user_input_ship():
    user_input = input("Введите характеристики корабля: ")
    if len(user_input) < 7 or len(user_input) > 8:
        return False
    try:
        user_input = list(map(int, user_input.split()))
    except ValueError:
        return False
    if len(user_input) < 4:
        return False
    else:
        return tuple(user_input)


def user_input_shot():
    user_input = input("Введите координаты выстрела: ")
    if len(user_input) < 3 or len(user_input) > 4:
        return False
    try:
        user_input = list(map(int, user_input.split()))
    except ValueError:
        return False
    if len(user_input) < 2:
        return False
    elif 1 <= user_input[0] <= 6 and 1 <= user_input[1] <= 6:
        return tuple(user_input)
    else:
        return False


if __name__ == '__main__':
    player = PlayerCanvas(False)
    computer = ComputerCanvas(True)

    print("""Приветстую, это игра Морской Бой. Вы будете играть с компьютером. 
Правила игры:
1)На поле распологается:
    -один трехпалубный корабль
    -два двухпалубных коробля
    -четыре однопалубных коробля 
2)Расстановка кораблей:
    -Расстояние между кораблями должно быть минимум в две клетки
    -Игрок расставляет корабли вручную или автоматически. 
     Формат ввода: x, y - координаты начальной палубы корабля
                   тип корабля(1-однопалубный, 2-двухпалубный, 3-трехпалубный)
                   поворот корабля(1 - горизонтальное положение корабля
                                   2 - вертикальное положение корабля
     Например, при вводе:3 4 2 1 
                         на поле игрока появиться корабль с начальными координатами(x=3, y=4)
                         двухпалубный с длиной две клетки
                         в горизонтальном положении
                         конечные координаты всех палуб коробля будут: ((3,4),(3,5))
     Если, например, будет такой ввод:6 5 3 1, корабль не появиться
                     так как он будет распологаться за пределами игрового поля.
    -Компьютер расставляет корабли случайным образом
3)Стрельба:
    -Игрок стреляет с помощью ввода координат выстрела, например:3 4
     Попадания отображаются, как: X
     Промахи отображаются, как: T
    -Компьютер стреляет автоматически
4)Побеждает тот, кто раньше разгромит флот противника.
Хорошей игры!
""")
    print("Ваше поле:")
    player.draw_canvas()
    while True:
        user_placement = input("Если хотите, чтобы корабли расставились автоматически введите-A, если вручную-M \n")
        if user_placement == 'A':
            print("Автоматическая расстановка")
            player.auto_ships_placement()
            break
        elif user_placement == "M":
            print("Ручная расстановка")
            player.draw_canvas()
            counter = 0
            while True:
                u_i = user_input_ship()
                if not u_i:
                    print("Недопустимый формат ввода")
                else:
                    temp_ship = Ship(*u_i)
                    check_add_ship = player.check_add_ship(temp_ship)
                    if check_add_ship == 'access':
                        player.add_ship(temp_ship)
                        counter += 1
                        player.draw_canvas()
                    else:
                        print(check_add_ship)
                if counter >= 7:
                    break
            break
        else:
            print("Некорректный формат ввода")
    print("Ваше поле после расстановки:")
    player.draw_canvas()
    print("Поле противника:")
    computer.draw_canvas()
    print("Игра начинается! Первым ходит игрок!\n")
    player_shot_base = CoordinateDict()
    player_shot_base.update(0, 0, 0)
    while True:
        while True:
            u_i = user_input_shot()
            if not u_i:
                print("Недопустимый формат ввода")
            elif not player_shot_base.find(*u_i):
                computer.shot(*u_i)
                player_shot_base.update(*u_i)
                break
            else:
                print("Вы уже стреляли в данную точку")
        print("Поле противника после выстрела:")
        computer.draw_canvas()
        if computer.defeat():
            print("Победил игрок! Поздравляю")
            print("Ваше поле:")
            player.draw_canvas()
            print("Поле противника:")
            computer.draw_canvas()
            break
        print("Стреляет компьютер", "\n", "Ваше поле:")
        computer_shot = computer.computer_shoot()
        player.shot(*computer_shot)
        player.draw_canvas()
        if player.defeat():
            print("Победил противник!")
            print("Ваше поле:")
            player.draw_canvas()
            print("Поле противника:")
            computer.draw_visible()
            break
