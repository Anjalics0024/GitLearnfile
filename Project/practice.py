import random

def play():
    user = input("What is your choice  1. Rock for r 2.Paper for P 3.Scissor for S")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a Tie '

    if is_win(user,computer):
        print("You WOn!")

    print("You loss")


def is_win(player, opponent):
    #return true if player win
    # p>r , S>p , r>s
    if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
        return True



print(play())
