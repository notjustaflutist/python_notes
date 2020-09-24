"""Tic-tac-toe game
9.14.2020
Alyssa Lada
"""

import random


def create_new_board():
    board = "A1|A2|A3\nB1|B2|B3\nC1|C2|C3\n"
    return board


def check_winner(board):
    result = False
    li = board.split("\n")
    for i in range(len(li)):
        li[i] = li[i].split("|")
    li.pop()

    if board.count("X") >= 3 or board.count("O") >= 3:
        for i in range(3):
            # horizontal win
            if li[i][0] == li[i][1] == li[i][2]:
                print("Horizontal line win!")
                result = True
                break
            # vertical win
            elif li[0][i] == li[1][i] == li[2][i]:
                print("Vertical line win!")
                result = True
                break
            # diagonal win
            elif li[0][0] == li[1][1] == li[2][2] or li[0][2] == li[1][1] == li[2][0]:
                print("Diagonal line win!")
                result = True
                break
    return result


def play_game():
    board = create_new_board()
    li = board.split("\n")
    for i in range(len(li)):
        li[i] = li[i].split("|")
    li.pop()
    comp_array = li.copy()

    print("Tic-Tac-Toe")
    player = str.upper(input("Play as X or O? "))
    if player == "X":
        comp = "O"
    else:
        comp = "X"
    print(f"Player: {player}\nComputer: {comp}\n")
    # print(f"{players[random.randint(0, 1)]} goes first!")
    print(board)
    has_winner = False
    out_of_moves = False
    while not has_winner and not out_of_moves:
        move_success = False
        while not move_success and not has_winner and not out_of_moves:
            move = str.upper(input("Choose a square: "))
            if move in board:
                board = board.replace(move, " " + player)
                print(f"You played {move}")
                print(board)
                move_success = True

        comp_move_success = False
        while not comp_move_success and not has_winner and not out_of_moves:
            comp_move = comp_array[random.randint(0, 2)][random.randint(0, 2)]
            if comp_move in board:
                board = board.replace(comp_move, " " + comp)
                print(f"Computer played {comp_move}")
                print(board)
                comp_move_success = True
                has_winner = check_winner(board)

        if board.count("X") == 5 or board.count("O") == 5:
            print("No more moves!")
            out_of_moves = True
    replay(str.upper(input("Play again? Y/N: ")))


def replay(response):
    if response == "N":
        exit(0)
    else:
        print("" * 2)
        play_game()


play_game()