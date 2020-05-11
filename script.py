def init_board(n, p):
    board = []

    # Make sure that there are empty spaces between the two players
    while p >= n // 2:
        p = n // 2 - 1

    middle_space = n - (p * 2)
    board = init_append_element(1, p, board)
    board = init_append_element(0, middle_space, board)
    board = init_append_element(2, p, board)

    return board


def init_append_element(element_type, element_quantity, board):
    for case in range(element_quantity):
        board.append(element_type)

    return board


def display(board, n):
    for number in range(1, n+1):
        print(number, end=" ")

    print()

    for index in range(n):
        case = board[index]

        if index >= 9:
            placeholder = "  "
        else:
            placeholder = " "

        if case == 1:
            print("x", end=placeholder)
        elif case == 0:
            print(".", end=placeholder)
        elif case == 2:
            print("o", end=placeholder)


def possible(board, n, i, player):
    i = i-1
    way = 0
    enemy_player = 0

    # Determine which way the player must go and who is his enemy
    if player == 1:
        way = 1
        enemy_player = 2
    elif player == 2:
        way = -1
        enemy_player = 1

    if board[i] != player:
        return False

    # Check the pattern Player->Enemy->Empty or -> Player->Empty
    if board[i + way] == 0:
        return i + way
    elif board[i + way] == enemy_player and board[i + way * 2] == 0:
        return i + way * 2
    else:
        return False


def select(board, n, player):
    number_is_invalid = True
    while number_is_invalid:
        number = int(input("Choose one of your pawns: "))
        print("----------")
        valid_number = possible(board, n, number, player)

        if type(valid_number) is int:
            number_is_invalid = False
            print(number)
            return number


def move(board, n, player, i):
    target = possible(board, n, i, player)
    board[i-1] = 0
    board[target] = player


def again(board, n, player):
    has_solution = False
    for x in range(n):
        if board[x] == player:
            check = possible(board, n, x+1, player)
            if type(check) == int:
                has_solution = True
    return has_solution


def switch_player(current_player):
    if current_player == 1:
        return 2
    elif current_player == 2:
        return 1


def toads_and_frogs(n, p):
    test = False
    if test:
        board = [1, 1, 1, 0, 0, 1, 2, 0, 0, 2, 2, 2]
    else:
        board = init_board(n, p)

    player_one_can_play = again(board, n, 1)
    player_two_can_play = again(board, n, 2)
    can_play_game = player_one_can_play and player_two_can_play
    current_player = 1

    print("----------")
    print("It's Player {}'s turn !".format(current_player))
    display(board, n)
    number = select(board, n, current_player)
    move(board, n, current_player, number)
    current_player = switch_player(current_player)

    while can_play_game:
        print("----------")
        print("It's Player {}'s turn !".format(current_player))
        display(board, n)
        number = select(board, n, current_player)
        move(board, n, current_player, number)
        if can_play_game:
            current_player = switch_player(current_player)


if __name__ == '__main__':
    toads_and_frogs(12, 4)
