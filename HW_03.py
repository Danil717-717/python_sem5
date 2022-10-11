# 3. * Создайте программу для игры в "Крестики-нолики".
#      Поле 3x3. Игрок - игрок, без бота.

board = list(map(str, range(1, 10)))


def draw_board():
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()


def place_sign(token):       # функция распологает элемент на поле выбирает и ставит ход
    global board             # переменная глобальная т.к внутри функции будет запрет на ее изменение 
    while True:              # проверки
        answer = input(f"Enter a number from 1 to 9.\nSelect a position {token}? ") # проверка в диапазоне от 1 до 9
        if answer.isdigit() and int(answer) in range(1, 10):                        # проверка введено ли вообще число
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):                              # проверка если уже не занята позиция крестиком ноликом
                board[answer - 1] = chr(10060) if token == "X" else chr(11093)   # если все ок то выставляем в данную позицию крестик нолик 
                break        # сверху тернарный оператор: если выражение истина, делаем что слева, если ложно то что после else
            else:
                print(f"This cell is already occupied{chr(9995)}{chr(129292)}")
        else:
            print(f"Incorrect input{chr(9940)}. Are you sure you entered a correct number?")


def check_win():        # функция определения выигрыша
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # кортежи с выигрышными позициями
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n


def main():
    counter = 0                # счетчик ходов для состояния возможной нечьи или другого
    draw_board()               # отрисовка доски
    while True:
        place_sign("O") if counter % 2 else place_sign("X")  # определение по сетности кто ходит
        draw_board()           # обязательно переотрисовка поля после хода

        if counter > 3:       # проверка после 3 ходов на возможность победы
            if check_win():
                print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
                break         # выход только по ничье или победе
        if counter == 8:
            print(f"Drawn game {chr(129318)}{chr(129309)}!")
            break             # выход только по ничье или победе
        counter += 1


main()             # стартуем с основного меню