def print_game(igra):
    vrednosti = {1: " X ",
                 -1: " O ",
                 0: "   "}
    for red in igra:
        print("|", end="")
        for i in red:
            print(vrednosti[i], end="")
            print("|", end="")
        print()


def is_over(igra):
    """
    Funkcija koja utvrdjuje da li je gotova partija.

    :param igra:
    :return: 1 ako je pobedio X, -1 ako je pobedio O ili 0 ako je nereseno.
    """
    # checking for rows sequence
    for red in igra:
        if red[0] == red[1] == red[2]:
            if red[0] == 1:
                return 1
            elif red[0] == -1:
                return -1
    # checking for columns sequence
    for i in range(3):
        if igra[0][i] == igra[1][i] == igra[2][i]:
            if igra[0][i] == 1:
                return 1
            elif igra[0][i] == -1:
                return -1
    # checking for diagonal sequence
    if igra[0][0] == igra[1][1] == igra[2][2]:
        if igra[0][0] == 1:
            return 1
        elif igra[0][0] == -1:
            return -1
    elif igra[0][2] == igra[1][1] == igra[2][0]:
        if igra[1][1] == 1:
            return 1
        elif igra[1][1] == -1:
            return -1
    else:
        return 0


def tabla():
    game = [[-1, 0, 1],
            [1, -1, -1],
            [-1, 0, -1]]
    print_game(game)
    print(is_over(game))

    game = [[0, 0, 1],
            [1, 0, 0],
            [-1, 0, 1]]
    print_game(game)
    print(is_over(game))

    game = [[0, 0, -1],
            [-1, -1, 1],
            [-1, 0, 1]]
    print_game(game)
    print(is_over(game))


def main():
    print("Welcome to Tick tack toe!")
    player1 = input("Please, pick a marker 'X' or 'O': ")
    player2 = ""
    if player1.upper() == 'X':
        player2 = "O"
        print("Player 1 will go first")
    else:
        player2 = "X"
        print("Player 2 will go first")
    x_or_o = 1
    moves = 0
    start = ""
    position_list = []
    while start.upper() != "YES":
        start = input("Click YES when you are ready to play: ")
    # number_list = [x for x in range(1, 10)]
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    # x is 1 and o is -1
    print_game(game)
    while moves < 10:
        if moves % 2:
            x_or_o = -1
        else:
            x_or_o = 1
        position = int(input("Choose your position. Type a number between 1 and 9: "))
        while position in position_list:
            position = int(input("Unavailable position! Type another number between 1 and 9: "))
        position_list.append(position)
        game[(position - 1) // 3][(position - 1) % 3] = x_or_o
        moves += 1
        print_game(game)
        if moves > 4:
            if is_over(game) == 1 or is_over(game) == -1:
                print("Congratulations!!! You have won the game.")
                break
    print("Game over!")


if __name__ == '__main__':
    main()
    # tabla()
