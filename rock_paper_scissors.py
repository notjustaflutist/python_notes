"""Rock Paper Scissors Game (scratch)
9.15.2020
Alyssa Lada
"""
import random
choices = "RPS"
winners = {
    "R": "S",
    "P": "R",
    "S": "P"
}


def play_game():
    player = player_choose()
    print(compare(player))
    replay = str.upper(input("Play again? Y/N: "))
    if replay == "Y":
        play_game()
    else:
        exit(0)


def player_choose():
    player = " "
    while player not in choices:
        player = str.upper(input("Choose Rock, Paper, or Scissors (R/P/S): "))
    return player


def compare(player):
    comp = choices[random.randint(0, 2)]
    result = ""
    print(f"Computer: {comp}\nPlayer: {player}")
    if player == "R":
        if comp == "R":
            result = "Tie"
        elif comp == "P":
            result = "Paper beats rock. You lose."
        else:
            result = "Rock beats scissors. You win."
    elif player == "P":
        if comp == "R":
            result = "Paper beats rock. You win."
        elif comp == "P":
            result = "Tie"
        else:
            result = "Scissors beats paper. You lose."
    else:
        if comp == "R":
            result = "Rock beats scissors. You lose."
        elif comp == "P":
            result = "Scissors beats paper. You win."
        else:
            result = "Tie"
    return result


play_game()