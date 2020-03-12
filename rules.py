""""
Author: Evan Gibson
Purpose: Set win conditions and rules for player behavior that don't initiate

"""

# Create class for checking board game for win conditions
class diaglysis:
    def __init__(self,
                 board_array, # the board is the only thing that needs to checked for win conditions
                 player_value, # The integer or float that corresponds to this player's checker marker
                 last_play, # The board coordinate for the last play position, we only need to check the last position
                 num_check_win = 4 # The number of adjacent tiles that create a win condition
                 ):
        self.array = board_array
        self.play_v = player_value
        self.win_c = num_check_win

        # Interpreted as a two item list indexable iterable
        self.position = last_play

    def down_right(self):
        # Execution function for down and right check
        dr = lambda d, x, y:tuple([x+d, y+d])

        # Trying is necessary because we will often index outside of allowable limits
        try:
            value_point = [self.array[dr(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False

    def down_left(self):
        # Execution function for down and right check
        dl = lambda d, x, y:tuple([x-d, y+d])

        # Trying is necessary because we will often index outside of allowable limits
        try:
            value_point = [self.array[dl(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False

    def up_left(self):
        # Execution function for down and right check
        ul = lambda d, x, y:tuple([x-d, y-d])

        # Trying is necessary because we will often index outside of allowable limits
        try:
            value_point = [self.array[ul(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False

    def up_right(self):
        # Execution function for down and right check
        ur = lambda d, x, y:tuple([x+d, y-d])

        # Trying is necessary because we will often index outside of allowable limits
        try:
            value_point = [self.array[ur(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False


    def just_right(self):
        jr = lambda d, x, y: tuple([x, y+d])
        try:
            value_point = [self.array[jr(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False

    def just_left(self):
        jl = lambda d, x, y: tuple([x, y-d])
        try:
            value_point = [self.array[jl(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False

    def just_down(self):
        jd = lambda d, x, y: tuple([x+d, y])
        try:
            value_point = [self.array[jd(n, self.position[0], self.position[1])] for n in range(self.win_c)]

        except:
            return False

        # Condition for win is calculated by getting the player's value multipled by the number of spaces he/she has in this row
        if (self.win_c * self.play_v) == sum(value_point):
            return True

        else:
            return False

    # We don't need a just_up function because it won't ever flag true



