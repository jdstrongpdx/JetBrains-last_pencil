from random import randint


def main():
    """Main function to call sub-functions"""

    # get and validate initial pencil input
    pencils = pencil_valid()

    # get and validate player choice
    player = player_check()
    while pencils > 0:
        printer(pencils, player)
        if player == "John":
            pencils = update_pencils(pencils)
        else:
            bot_pencils = player_bot(pencils)
            print(bot_pencils)
            pencils -= bot_pencils
        player = switch_player(player)
    print(f"{player} won!")


def pencil_valid():
    """ Gets and validates input for the number of pencils
        :return (int) pencils: the number of pencils to start the game
    """

    while True:
        try:
            # get input and check if int and positive
            pencils = int(input("How many pencils would you like to use: "))
            # check if zero
            if pencils == 0:
                print("The number of pencils should be positive")
            else:
                return pencils
        except TypeError and ValueError:
            print("The number of pencils should be numeric")


def player_check():
    """ Gets and validates player name input
        :return (str) player: chooses which player will begin the game
    """

    while True:
        try:
            player_names = ["John", "Jack"]
            player = input("Who will be the first (John, Jack):")
            if player not in player_names:
                print("Choose between *Name1* and *Name2*")
            else:
                return player
        except TypeError:
            pass


def printer(pencil_count, player_name):
    """ Prints number of pencils remaining followed by next players turn.
        :parameter (int) pencil_count: the number of pencils to print
        :parameter (str) player_name: the name of the user to print
        :return: None
    """

    for i in range(pencil_count):
        print("|", end="")
    print()   # for new line
    print(f"{player_name}'s turn:")


def switch_player(player_name):
    """ Switches the user after each turn
        :parameter (str) player_name: the name of the current player
        :return (str): the name of the player
    """

    if player_name == "John":
        return "Jack"
    else:
        return "John"


def update_pencils(pencil_count):
    """ Gets and validates the number of pencils chosen each turn
        :parameter (int) pencil_count: the number of pencils left in the game
        :return (int): the number of pencils left after current user choice
    """

    while True:
        try:
            num_allowed = [1, 2, 3]
            request = int(input())
            if request not in num_allowed:
                print("Possible values: '1', '2', or '3'")
            elif pencil_count - request < 0:
                print("Too many pencils were taken")
            else:
                return pencil_count - request
        except TypeError and ValueError:
            print("Possible values: '1', '2', or '3'")


def player_bot(pencil_count):
    """ Automates a second player with optimal rules for playing
        :parameter (int) pencil_count: the current number of pencils left in the game
        :return (int): returns the optimal number of pencils to take in a turn
    """

    if pencil_count == 1:   # exception
        return 1
    for sequence in range(2, 6):
        pencil_calc = (pencil_count - sequence)/4
        if pencil_calc == 0:   # base case
            if sequence == 5:
                return randint(1, 3)
            else:
                return sequence - 1
        elif int(pencil_calc) == pencil_calc:
            if sequence == 5:   # return "random"
                return randint(1, 3)
            else:
                return sequence - 1  # return sequence base


""" TESTING CODE FOR PLAYER_BOT 
one = [1]
two = [2, 6, 10, 14]
three = [3, 7, 11, 15]
four = [4, 8, 12, 16]
five = [5, 9, 13, 17]
for i in range(17):
    if i in one:
        print(i, player_bot(i) == 1)
    elif i in two:
        print(i, player_bot(i) == 1)
    elif i in three:
        print(i, player_bot(i) == 2)
    elif i in four:
        print(i, player_bot(i) == 3)
    elif i in five:
        print(i, player_bot(i) == (0 or 2))
"""

main()
