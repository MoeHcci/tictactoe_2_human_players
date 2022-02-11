from tictactoe_functions import boardtable
from tictactoe_functions import user_position
from tictactoe_functions import new_selection
from tictactoe_functions import keepplaying
from IPython.display import clear_output

def tictactoe_game():
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
    tictactoe_game()
