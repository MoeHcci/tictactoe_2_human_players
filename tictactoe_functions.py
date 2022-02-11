def boardtable(mainlist):
    print('The latest game layout is presented below: ')
    print("The board's layout is similar to keyboard's numeric keypay")
    print(*mainlist)


def user_position():
    choice = 'anything but a reasonable value that go into the list'

    while choice not in ['7', '8', '9', '4', '5', '6', '1', '2', '3']:
        choice = input("pick a number between 1-7 to represent the position: ")

        if choice not in ['7', '8', '9', '4', '5', '6', '1', '2', '3']:
            print('''sorry, pick a number between 1-7 to represent the position: ''')

        else:
            return int(choice)


def new_selection(mainlist, index_postion):
    new_index_selection = (input("Your turn enter x or o: "))
    if index_postion == 7:
        index_postion = 1
    elif index_postion == 8:
        index_postion = 3
    elif index_postion == 9:
        index_postion = 5
    elif index_postion == 4:
        index_postion = 9
    elif index_postion == 5:
        index_postion = 11
    elif index_postion == 6:
        index_postion = 13
    elif index_postion == 1:
        index_postion = 17
    elif index_postion == 2:
        index_postion = 19
    elif index_postion == 3:
        index_postion = 21
    mainlist[index_postion] = new_index_selection
    print(*mainlist)  # This line for visualization
    return mainlist  # return the updatted list, without this line nothing will work


def keepplaying():
    choice = 'anything but a reasonable value that go into the list'
    while choice not in ['y', 'n']:
        choice = input('Play again ? Enter (y or n): ')
        if choice not in ['y', 'n']:
            print('Your answer must be either y or n. You inputted something else')
    # if choice was in Y then return true
    if choice == 'y':
        print('Okay, lets play again')
        return True
    else:  # if the choice is 'No'
        print("Thank you for playing")
        return False


def tictactoe():
    from IPython.display import clear_output
    mainlist = ["\n", 7, "|", 8, "|", 9, "\n", "----------",
                "\n", 4, "|", 5, "|", 6, "\n", "----------",
                "\n", 1, "|", 2, "|", 3]

    # lists & tuples for the decision conditions
    x_player_winlist = ['x', 'x', 'x']
    o_player_winlist = ['o', 'o', 'o']
    x_w = tuple(x_player_winlist)
    o_w = tuple(o_player_winlist)
    # The draw conditions
    five_x = ('x', 'x', 'x', 'x', 'x')
    cont_five_x = five_x.count('x')  # = 5
    four_o = ('o', 'o', 'o', 'o')
    cont_four_o = four_o.count('o')  # = 4
    four_x = ('x', 'x', 'x', 'x')
    cont_four_x = four_x.count('x')  # = 4
    five_o = ('o', 'o', 'o', 'o', 'o')
    cont_five_o = five_o.count('o')  # = 5

    game_on = True
    while game_on == True:

        # Displaying the latest board
        boardtable(mainlist)

        # Index selection
        replacable_index = user_position()

        # Selected index variable replacement
        mainlist = new_selection(mainlist, replacable_index)

        # Clearing the screen
        clear_output()

        # Displaying the latest board after updating it
        boardtable(mainlist)

        # Winning lists, tuples, and logic
        HR1 = [mainlist[1], mainlist[3], mainlist[5]]
        HR2 = {mainlist[9], mainlist[11], mainlist[13]}
        HR3 = [mainlist[17], mainlist[19], mainlist[21]]
        VC1 = [mainlist[1], mainlist[9], mainlist[17]]
        VC2 = [mainlist[3], mainlist[11], mainlist[19]]
        VC3 = [mainlist[5], mainlist[13], mainlist[21]]
        D_L_R = [mainlist[1], mainlist[11], mainlist[21]]
        D_R_L = [mainlist[5], mainlist[11], mainlist[17]]
        # The conditions in which the game could be won
        hr1 = tuple(HR1)
        hr2 = tuple(HR2)
        hr3 = tuple(HR3)
        vc1 = tuple(VC1)
        vc2 = tuple(VC2)
        vc3 = tuple(VC3)
        d_l_r = tuple(D_L_R)
        d_r_l = tuple(D_R_L)

        # Winning logic
        if hr1 == x_w or hr2 == x_w or hr3 == x_w or vc1 == x_w or vc2 == x_w or vc3 == x_w or d_l_r == x_w or d_r_l == x_w:
            print('player x has won')
            game_on = False
        elif hr1 == o_w or hr2 == o_w or hr3 == o_w or vc1 == o_w or vc2 == o_w or vc3 == o_w or d_l_r == o_w or d_r_l == o_w:
            print('player o has won')
            game_on = False
        elif mainlist.count('x') == cont_five_x and mainlist.count('o') == cont_four_o:
            print('The game is a draw')
            game_on = False
        elif mainlist.count('x') == cont_four_x and mainlist.count('o') == cont_five_o:
            print('The game is a draw')
            game_on = False
        else:
            game_on = True
        # Playing again suggestion
        if game_on == False:
            mainlist = ["\n", 7, "|", 8, "|", 9, "\n", "----------",
                        "\n", 4, "|", 5, "|", 6, "\n", "----------",
                        "\n", 1, "|", 2, "|", 3]
            game_on = keepplaying()

if __name__ == '__main__':
    tictactoe()
