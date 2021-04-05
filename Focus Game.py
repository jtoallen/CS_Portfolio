#Author: Jason Allen
#Date: 20/11/2020
#Description: Focus Game.
"""
An Abstract Board Game made for 2 players on a 6x6 board.
First player to capture six opponent pieces wins. Any player may begin the game
Two players move stacks of one to five pieces around a checkerboard.
Stacks may move as many spaces as there are pieces in the stack.
Players may only move a stack if the topmost piece in the stack
is one of their pieces. When a stack lands on another stack,
the two stacks merge; if the new stack contains more than five pieces,
then pieces are removed from the bottom to bring it down to five.
If a player's own piece is removed, they are kept and may be placed
on the board later in lieu of moving a stack.
If an opponent's piece is removed, it is captured.
The first player to capture six opponent pieces wins the game.
"""


class FocusGame:
    """6X6 board. Green and Red Player Pieces called 'R' and 'G.
    Game has one class called FocusGame.  The methods of the class will manage
    progress of the game. Method types fall under these categories:
    get methods, validate logic, move piece, reserve piece, and capture piece.
    '"""

    def __init__(self, p1, p2):
        """
        An init method that takes as its parameters two tuples, each containing
        player name and color of the piece that player is playing
        (ex: ('PlayerA', 'R'), ('PlayerB','R')). It initializes the board
        with the pieces placed in the correct positions using a list of lists.
        The board positions start with (0,0) and end at (5,5).
        The top left corner position being
        (0,0) and bottom right corner position being (5,5).
        In (0,0) the first 0 represents row and second 0 represents column.
        The pieces are marked as R and G for Red and Green respectively --
        this is case insensitive. contains data attribute to hold player turn.
        default value for plyr turn is None. p1 is player 1, p2 is player 2
        attributes are player name, player color,
        p1 captured pieces default = 0, p2 captured pieces default = 0.
        player reserve default is 0. self._num_pcs is None and will be used
        for remove method pieces method. player turn default value is None
        """
        self._p1 = (p1)
        self._p2 = (p2)
        self._p1_name = (p1[0])
        self._p1_clr = (p1[1])
        self._p2_name = (p2[0])
        self._p2_clr = (p2[1])
        self._p1_reserve = 0
        self._p2_reserve = 0
        self._captured_by_p1 = 0
        self._captured_by_p2 = 0
        self._num_pcs = None
        self._plyr_turn = None
        self._board = \
        [
        [[p1[1]], [p1[1]], [p2[1]], [p2[1]], [p1[1]], [p1[1]]],
        [[p2[1]], [p2[1]], [p1[1]], [p1[1]], [p2[1]], [p2[1]]],
        [[p1[1]], [p1[1]], [p2[1]], [p2[1]], [p1[1]], [p1[1]]],
        [[p2[1]], [p2[1]], [p1[1]], [p1[1]], [p2[1]], [p2[1]]],
        [[p1[1]], [p1[1]], [p2[1]], [p2[1]], [p1[1]], [p1[1]]],
        [[p2[1]], [p2[1]], [p1[1]], [p1[1]], [p2[1]], [p2[1]]]
        ]


    def print(self):
        """takes no parameters. prints board in rows
        to depict visual representation of board
        method is used for testing"""
        for i in self._board:
            print(i)


    def get_board(self):
        """takes no parameters.
        used for checking location of player tokens and
        updating position of player tokens
        returns board"""
        return self._board


    def get_p1_name(self):
        """takes no parameters. used to check player turn,
        position of player tokens, status of a p1 win,
        check is p1 token is on top of stack.
        returns name for p1"""
        return self._p1_name


    def get_p2_name(self):
        """takes no parameters. used to check player turn,
        position of player tokens, status of a p2 win,
        check is p2 token is on top of stack.
        returns name for p2"""
        return self._p2_name


    def get_p1_clr(self):
        """takes no parameters.
        returns color for p1. used to check logic for move methods.
        helps make sure player name passed in move method
        is associated with player token at beginning position.
        returns player color for p1"""
        return self._p1_clr


    def get_p2_clr(self):
        """takes no parameters.
        returns color for p1. used to check logic for move methods.
        helps make sure player name passed in move method
        is associated with player token at beginning position.
        returns player color for p2"""
        return self._p2_clr


    def get_turn(self):
        """takes no parameters. keeps track of player turn.
        default value is None. player turn is updated after
        a successful player move.
        returns player name """
        return self._plyr_turn


    def get_hght(self, end):
        """takes parameter, pos, for position that
        player will move from. checks height of stack at position.
        used to validate if number of pieces player wants to move is less than
        or equal to the height of the stack at position
        returns int representing height of stack"""
        return len(self.get_board()[end[0]][end[1]])


    def check_p1_wins(self, plyr):
        """"checks if win conditions for p1 are met.
        accepts player name parameter.
        used in association with show captured method to check if
        captured pieces are 6 or greater
        returns player name + Wins"""
        self._plyr = plyr

        if self.show_captured(self._plyr) > 5:
            return self.get_p1_name() + " Wins"


    def check_p2_wins(self, plyr):
        """"checks if win conditions for p1 are met.
        accepts player name parameter.
        used in association with show captured method to check if
        captured pieces are 6 or greater
        returns player name + Wins"""
        self._plyr = plyr

        if self.show_captured(self._plyr) > 5:
            return self.get_p2_name() + " Wins"


    def check_diagonal_move(self, bgn, end, num_pcs):
        """helper method for move piece.
        accepts tuple for beginnng, bgn, ending, end, coordinates
         of desired move and number of pieces, num_pcs
        Checks if attempted move is in a diagonal.
        if move results in a diagonal move returns True.
        if move piece method receives True value, then it returns
        invalid location"""
        self._bgn = bgn
        self._end = end
        self._num_pcs = num_pcs
        self._row_changed = None
        self._column_changed = None
        self._num_pcs = num_pcs

        if bgn[0] == end[0] and bgn[1] + num_pcs == end[1]:
            self._column_changed = True
        if bgn[0] != end[0] and bgn[1] + num_pcs == end[1]:
            self._column_changed = True
            self._row_changed = True

        if bgn[0] == end[0] and bgn[1] - num_pcs == end[1]:
            self._column_changed = True
        if bgn[0] != end[0] and bgn[1] - num_pcs == end[1]:
            self._column_changed = True
            self._row_changed = True
            # print("both row and column changed")

        if bgn[0] + num_pcs == end[0] and bgn[1] == end[1]:
            self._row_changed = True
        if bgn[0] + num_pcs == end[0] and bgn[1] != end[1]:
            # print("both row and column changed")
            self._row_changed = True
            self._column_changed = True

        if bgn[0] - num_pcs == end[0] and bgn[1] == end[1]:
            self._row_changed = True
        if bgn[0] - num_pcs == end[0] and bgn[1] != end[1]:
            # print("both row and column changed")
            self._row_changed = True
            self._column_changed = True

        if self._row_changed is True and self._column_changed is True:
            # print("row and column changed")
            return True


    def single_move(self, plyr, bgn, end, num_pcs):
        """"helper method for move piece method.
        parameters: player name, tuple representing coordinates
        for beginning postion, tuple representing coordinates for end position,
        number of tokens player wishes to move.
        used for moving a player's single token.
        checks if player token in on top of stack in beginning position.
        calls check p1 wins method and calls check p2 wins method
        deletes player token from previous position.
        appends tokens to end position. updates player turn.
        returns 'successfully moved"""
        self._plyr = plyr
        self._bgn = self._board[bgn[0]][bgn[1]]
        self._end = self._board[end[0]][end[1]]
        self._num_pcs = num_pcs
        pos_pieces = None

        if self.get_turn() == self._p1_name:
            if self.get_p1_clr() == self._bgn[-1]:
                pos_pieces = self._bgn[-num_pcs:]
                del self._board[bgn[0]][bgn[1]][-num_pcs:]
                self._end += pos_pieces #concatentate new pieces to old position
                if self.get_hght(end) > 5:
                    self.remove_pieces(self._plyr, end, num_pcs)
                if self.check_p1_wins(self._plyr):
                    return self.check_p1_wins(self._plyr)
                self._plyr_turn = self.get_p2_name()
                return 'successfully moved'
            # else:
            # print('this is not your piece to move')
            return False

        if self.get_turn() == self._p2_name:
            if self.get_p2_clr() == self._bgn[-1]:
                pos_pieces = self._bgn[-num_pcs:]
                del self._board[bgn[0]][bgn[1]][-num_pcs:]
                self._end += pos_pieces #concatentate new pieces to old position
                if self.get_hght(end) > 5:
                    self.remove_pieces(self._plyr, end, num_pcs)
                if self.check_p2_wins(self._plyr):
                    return self.check_p2_wins(self._plyr)
                self._plyr_turn = self.get_p1_name()
                return 'successfully moved'
            # else:
            # print('this is not your piece to move')
            return False


    def multiple_move(self, plyr, bgn, end, num_pcs):
        """helper method for move piece method. used if player
        moves multiples tokens.
        parameters: player name, tuple representing coordinates
        for beginning postion, tuple representing coordinates for end position,
        number of tokens player wishes to move.
        used for moving a player's single token.
        checks if player token in on top of stack in beginning position.
        deletes player token from previous position.
        appends tokens to end position. updates player turn.
        returns 'successfully moved"""
        self._plyr = plyr
        self._bgn = self._board[bgn[0]][bgn[1]]
        self._end = self._board[end[0]][end[1]]
        self._num_pcs = num_pcs
        pos_pieces = None

        if self.get_turn() == self._p1_name:
            if self.get_p1_clr() == self._bgn[-1]:
                pos_pieces = self._bgn[-num_pcs:]
                # print(pos_pieces)
                # print(self._end)
                self._end += pos_pieces #concatentate new pieces to old position
                # print(self._end)
                if self.get_hght(end) > 5:
                    self.remove_pieces(self._plyr, end, num_pcs)
                del self._board[bgn[0]][bgn[1]][-num_pcs:]
                if self.check_p1_wins(self._plyr):
                    return self.check_p1_wins(self._plyr)
                self._plyr_turn = self.get_p2_name()
                return 'successfully moved'
            else:
                return False

        if self.get_turn() == self._p2_name:
            if self.get_p2_clr() == self._bgn[-1]:
                pos_pieces = self._bgn[-num_pcs:]
                self._end += pos_pieces #concatentate new pieces to old position
                if self.get_hght(end) > 5:
                    self.remove_pieces(self._plyr, end, num_pcs)
                del self._board[bgn[0]][bgn[1]][-num_pcs:]
                if self.check_p2_wins(self._plyr):
                    return self.check_p2_wins(self._plyr)
                self._plyr_turn = self.get_p1_name()
                return 'successfully moved'
            else:
                return False


    def check_boundaries(self, plyr, bgn, end, num_pcs):
        """checks to make sure move is on the board
        takes 4 parameters: player, tuple of begin position,
        tuple of end position, num of pieces to move"""
        self._plyr = plyr
        self._bgn = bgn
        self._end = end
        self._num_pcs = num_pcs

        if bgn[0] not in range(0,6):
            # print('this move is out of bounds')
            return False
        if bgn[1] not in range(0, 6):
            # print('this move is out of bounds')
            return False
        if end[0] not in range(0,6):
            # print('this move is out of bounds')
            return False
        if end[1] not in range(0, 6):
            # print('this move is out of bounds')
            return False


    def legal_move(self, plyr, bgn, end, num_pcs):
        """check is space is blank with 0 pieces to move.
        checks if player tries to move 0 spaces
        checks if num pieces equal to num squares moved"""
        start_pos = len(self._board[bgn[0]][bgn[1]])
        self._plyr = plyr
        self._bgn = bgn
        self._end = end
        self._num_pcs = num_pcs

        #space has 0 pieces to move
        if start_pos == 0:
            return False

        #tries to move 0 spaces:
        if bgn[0] == end[0] and bgn[1] == end[1]:
            return False

        #if player tries to move more squares than pieces
        #check if num_pcs + end[0]end[1]
        if bgn[0] + num_pcs != abs(end[0]) and bgn[1] + num_pcs != abs(end[1]) and \
            bgn[0] - num_pcs != abs(end[0]) and bgn[1] - num_pcs != abs(end[1]):
                # print("num pieces must equal num spaces ")
                return False


    def move_piece(self, plyr, bgn, end, num_pcs):
        """:parameters in order: plyr is player name making move,
        bgn is tuple of beginning coordinates,
        end is tuple of destination coordinates,
        num_pieces is an integer representing number pieces being moved.
        used to move player tokens. passes parameters and calls single
        move method and multiple move methods to make logic clear and concise.
        updates player turn after first move.
        calls get turn method to validate player turn
        calls get hght method to validate number of pieces moved,
        calls check diagonal method to validate move,
        calls remove pieces method to capture pieces,
        returns one of the following:
        'not your turn', 'invalid location' 'invalid number of pieces',
        'successfully move'
        p1 'wins', or  p2 'wins'."""
        self._plyr = plyr
        self._bgn = bgn
        self._end = end
        self._num_pcs = num_pcs

        if self.get_turn() is None: #set to player who makes first move of game
            self._plyr_turn = self._plyr

        if self.get_turn() != self._plyr:
            return False

        if self.check_boundaries(plyr, bgn, end, num_pcs) is False:
            return False

        if self.legal_move(plyr, bgn, end, num_pcs) is False:
            return False

        if self._num_pcs > self.get_hght(bgn):
            return False

        if self._num_pcs == 0:
            return False

        if self.check_diagonal_move(bgn, end, num_pcs) is True:
            return False

        if self._num_pcs == 1:
            return self.single_move(plyr, bgn, end, num_pcs)

        if self._num_pcs > 1:
            return self.multiple_move(plyr, bgn, end, num_pcs)


    def show_pieces(self, pos):
        """:parameter takes a position on the board
         0th index is the bottom-most piece of the stack of pieces.
         returns list showing pieces present at position."""
        self._position = pos
        return self.get_board()[pos[0]][pos[1]]


    def show_reserve(self, plyr):
        """:parameter plyr is the player's name.
        shows count of pieces that are in reserve for plyr.
        If 0 in reserve returns 0 which is default value.
        returns int representing number of pieces in reserve"""
        self._plyr = plyr

        if self._plyr == self.get_p1_name():
            return self._p1_reserve

        if self._plyr == self.get_p2_name():
            return self._p2_reserve


    def show_captured(self, plyr):
        """:parameter. takes one param: plyr is player's name.
        shows number of pieces captured by player.
        If none captured, return 0, else returns int representing
        number of opponent's pieces that have been captured"""
        self._plyr = plyr

        if self._plyr == self.get_p1_name():
            return self._captured_by_p1

        if self._plyr == self.get_p2_name():
            return self._captured_by_p2


    def remove_pieces(self, plyr, end, num_pcs):
        """"if stack height is greater than 5
        slice the list at end position until only 5 tokens left.
        take a slice of list for removed pcs and saved pcs
        iterate over removed pcs list distribute pieces to reserved or captured
        based on whether or not the removed tokens match the player turn.
        empty list slice. return respective values to
        player reserve and captured by player attributes"""
        self._end = end
        self._plyr = plyr
        removed = []
        saved = []
        self._num_pcs = num_pcs
        length = len(self.get_board()[end[0]][end[1]])

        num_to_remv = length - 5
        # print('number to remove is', num_to_remv)
        removed = self.get_board()[end[0]][end[1]][:num_to_remv]
        saved = self.get_board()[end[0]][end[1]][num_to_remv:]
        # print("removed is ", removed)
        # print("saved is ", saved)
        self.get_board()[end[0]][end[1]] = saved

        #Update player reserve and player captured tokens
        if self.get_turn() == self.get_p1_name():
            for k in removed:
                if k == self.get_p1_clr():
                    self._p1_reserve +=1
                if k != self.get_p1_clr():
                    self._captured_by_p1 +=1
        if self.get_turn() == self.get_p2_name():
            for k in removed:
                if k == self.get_p2_clr():
                    self._p2_reserve +=1
                if k != self.get_p2_clr():
                    self._captured_by_p2 +=1


    def reserved_move(self, plyr, end, num_pcs = 1):
        """:parameter:3 params plyr is player's name.
        end is position on board.
        num_pcs is always be 1. Places one piece from reserve at end position.
        Reduces number of reserves pieces by one.
        Updates pieces at location. If no pieces in reserve
        returns 'no pieces in reserve'"""
        self._plyr = plyr
        self._end = end
        # self._end = self._board[end[0]][end[1]]
        self._num_pcs = 1

        if self.check_boundaries(plyr, end, end, num_pcs) is False:
            return False

        if self.show_reserve(self._plyr) == 0:
            return False

        if self.get_turn() != self._plyr:
            return False

        if self.get_turn() == self._p1_name:
            self._board[end[0]][end[1]] += self._p1_clr #concatentate new piece
            #check get height method
            #check remove pieces method
            #check p1 wins method
            if self.get_hght(end) > 5:
                self.remove_pieces(self._plyr, end, num_pcs)
            if self.check_p1_wins(self._plyr):
                return self.check_p1_wins(self._plyr)
            self._p1_reserve -=1
            self._plyr_turn = self.get_p2_name()
            return 'successfully moved'

        if self.get_turn() == self._p2_name:
            self._board[end[0]][end[1]] += self._p2_clr #concatentate new piece
            #check get height method
            #check remove pieces method
            #check p2 wins method
            if self.get_hght(end) > 5:
                self.remove_pieces(self._plyr, end, num_pcs)
            if self.check_p2_wins(self._plyr):
                return self.check_p2_wins(self._plyr)
            self._p2_reserve -=1
            self._plyr_turn = self.get_p1_name()
            return 'successfully moved'


# #testing function

def main():
    game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
    game.print()

if __name__ == '__main__':
    main()

