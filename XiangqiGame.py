# Author: Mo Abid
# Date: March 2, 2020
# Description:
class XiangqiGame:
    def __init__(self):
        self._game_state = 'UNFINISHED'
        self._check_red = False
        self._check_black = False
        self._red_general = General(9,4,'g') #starting player is red
        self._turn = 'red'
        self._black_general = General(0,4,'G') #Uppercase is black
        self._board = [[Chariot(0, 0, 'C'), Horse(0, 1, 'H'), Elephant(0, 2, 'E'), Advisor(0, 3, 'A'), General(0, 4, 'G'),
                  Advisor(0, 5, 'A'), Elephant(0, 6, 'E'), Horse(0, 7, 'H'), Chariot(0, 8, 'C')],
                 [None, None, None, None, None, None, None, None, None],
                 [None, Cannon(2, 1, 'N'), None, None, None, None, None, Cannon(2, 7, 'N'), None],
                 [Soldier(3, 0, 'S'), None, Soldier(3, 2, 'S'), None, Soldier(3, 4, 'S'), None, Soldier(3, 6, 'S'),
                  None, Soldier(3, 8, 'S')],
                 [None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None],
                 [Soldier(6, 0, 's'), None, Soldier(6, 2, 's'), None, Soldier(6, 4, 's'), None, Soldier(6, 6, 's'),
                  None, Soldier(6, 8, 's')],
                 [None, Cannon(7, 1, 'n'), None, None, None, None, None, Cannon(7, 7, 'n'), None],
                 [None, None, None, None, None, None, None, None, None],
                 [Chariot(9, 0, 'c'), Horse(9, 1, 'h'), Elephant(9, 2, 'e'), Advisor(9, 3, 'a'), General(9, 4, 'g'),
                  Advisor(9, 5, 'a'), Elephant(9, 6, 'e'), Horse(9, 7, 'h'), Cannon(9, 8, 'n')]]

        # starting board will be represented by the respective objects of each piece
                       # board[0][3] to board [0][5] by board [2][3] to board[2][5] is the palace
                       # board[7][3] to board [7][5] by board[9][3] to board[9][5] is the opposing palace
            # this dictionary will convert algebraic form into a
        self._coordinates = {
                'a10': (0, 0),
                'b10': (0, 1),
                'c10': (0, 2),
                'd10': (0, 3),
                'e10': (0, 4),
                'f10': (0, 5),
                'g10': (0, 6),
                'h10': (0, 7),
                'i10': (0, 8),

                'a9': (1, 0),
                'b9': (1, 1),
                'c9': (1, 2),
                'd9': (1, 3),
                'e9': (1, 4),
                'f9': (1, 5),
                'g9': (1, 6),
                'h9': (1, 7),
                'i9': (1, 8),

                'a8': (2, 0),
                'b8': (2, 1),
                'c8': (2, 2),
                'd8': (2, 3),
                'e8': (2, 4),
                'f8': (2, 5),
                'g8': (2, 6),
                'h8': (2, 7),
                'i8': (2, 8),

                'a7': (3, 0),
                'b7': (3, 1),
                'c7': (3, 2),
                'd7': (3, 3),
                'e7': (3, 4),
                'f7': (3, 5),
                'g7': (3, 6),
                'h7': (3, 7),
                'i7': (3, 8),

                'a6': (4, 0),
                'b6': (4, 1),
                'c6': (4, 2),
                'd6': (4, 3),
                'e6': (4, 4),
                'f6': (4, 5),
                'g6': (4, 6),
                'h6': (4, 7),
                'i6': (4, 8),

                'a5': (5, 0),
                'b5': (5, 1),
                'c5': (5, 2),
                'd5': (5, 3),
                'e5': (5, 4),
                'f5': (5, 5),
                'g5': (5, 6),
                'h5': (5, 7),
                'i5': (5, 8),

                'a4': (6, 0),
                'b4': (6, 1),
                'c4': (6, 2),
                'd4': (6, 3),
                'e4': (6, 4),
                'f4': (6, 5),
                'g4': (6, 6),
                'h4': (6, 7),
                'i4': (6, 8),

                'a3': (7, 0),
                'b3': (7, 1),
                'c3': (7, 2),
                'd3': (7, 3),
                'e3': (7, 4),
                'f3': (7, 5),
                'g3': (7, 6),
                'h3': (7, 7),
                'i3': (7, 8),

                'a2': (8, 0),
                'b2': (8, 1),
                'c2': (8, 2),
                'd2': (8, 3),
                'e2': (8, 4),
                'f2': (8, 5),
                'g2': (8, 6),
                'h2': (8, 7),
                'i2': (8, 8),

                'a1': (9, 0),
                'b1': (9, 1),
                'c1': (9, 2),
                'd1': (9, 3),
                'e1': (9, 4),
                'f1': (9, 5),
                'g1': (9, 6),
                'h1': (9, 7),
                'i1': (9, 8),
            }  #tuple with the respective coordinates of the board

    def print(self):
        for row in self._board:
            for value in row:
                if(value is not None):
                    print(value, end = "")
                else:
                    print(" ", end = "")
            print()

    def find_black_general(self,board):
        for row in board:
            for piece in row:
                if piece is not None and piece.get_symbol() == 'G':
                    return piece

    def find_red_general(self,board):
        for row in board:
            for piece in row:
                if piece is not None and piece.get_symbol() == 'g':
                    return piece

    def deepcopy(self,array): #faster method for deepcopying using list slicing
        y = [row[:] for row in array]
        return y

    def make_move(self,coordinate_at, coordinate_to):
        if(not self._game_state == 'UNFINISHED'):
            return False
        index_at = self._coordinates[coordinate_at] # (row, col)
        index_to = self._coordinates[coordinate_to] #(row, col)
        if(self._board[index_at[0]][index_at[1]] is None): #no piece at coordinate indicated
            return False
        if(not self._board[index_at[0]][index_at[1]].get_team() == self._turn):
            return False
        test_board = self.deepcopy(self._board)
        if(self._board[index_at[0]][index_at[1]].get_team() == 'red'):
            if(test_board[index_at[0]][index_at[1]].move(index_to[0],index_to[1],test_board)): #if move follows the rules
                if(not self.check_for_check('red',test_board)): #if move doesn't leave player in check
                    self._check_red = False
                    self._board[index_at[0]][index_at[1]].move(index_to[0], index_to[1],self._board)  # actually move the piece
                    #now that the player's move is valid, check if it put the other team in check
                    self._check_black = self.check_for_check('black',self._board)
                    if(self._check_black):
                        if(self.check_for_checkmate('black')):
                            self._game_state = 'RED_WON'
                    self._turn = 'black' #now it's black's turn because red made a successful move
                    return True
                else:
                    if (self._check_red == False):  # if they can't make a move because it would put general in check, could be stalemate
                        if (self.check_for_checkmate('red')):  # check for stalemate using the checkmate rules, because not moving is not a valid move, so
                            self._game_state = 'BLACK_WON'
                    return False #can't move a piece if it leaves your general in check
            return False
        if(self._board[index_at[0]][index_at[1]].get_team() == 'black'):
            if(test_board[index_at[0]][index_at[1]].move(index_to[0], index_to[1], test_board)): #if move follows rules
                if(not self.check_for_check('black', test_board)): #if move doesn't put in check
                    self._check_black = False
                    self._board[index_at[0]][index_at[1]].move(index_to[0], index_to[1], self._board) #actually move the piece
                    #now that the player's move is valid, check if it put the other team in check
                    self._check_red = self.check_for_check('red', self._board)
                    if (self._check_red): #check if it was a winning move
                        if (self.check_for_checkmate('red')):
                            self._game_state = 'BLACK_WON'
                    self._turn = 'red' #now it's red's turn because black made a successful move
                    return True
                else:
                    if(self._check_black == False): #if they can't make a move because it would put general in check, could be stalemate
                        if(self.check_for_checkmate('black')): #check for stalemate using the checkmate rules, because not moving is not a valid move, so
                            self._game_state = 'RED_WON'
                    return False #can't move a piece if it leaves your general in check
            return False

    def check_for_check(self,team,board):
        '''
            :param team: either red or black, if called with red will check if red general is in check and vice versa
            This method checks to see if any opposing piece could take a team's general on their next move.
            '''
        #check if the team's general is in check (so if called with red, will check if red general is in check)
        if(team == 'black'):
            for row in board:
                for piece in row:
                    if(piece is not None and piece.get_team() == 'red'):
                        if(self.valid_move(piece, self.find_black_general(board).get_pos()[0], self.find_black_general(board).get_pos()[1], board)):
                            return True
            return False
        if (team == 'red'):
            for row in board:
                for piece in row:
                    if (piece is not None and piece.get_team() == 'black'):
                        if (self.valid_move(piece, self.find_red_general(board).get_pos()[0], self.find_red_general(board).get_pos()[1],board)):
                            return True
            return False

    def valid_move(self,piece,row_to,col_to,board): #can't directly mutate board when checking for moves
        b = self.deepcopy(board)
        if(piece.move(row_to,col_to,b) and (not piece.get_pos() == [row_to,col_to])): #checks to see that the valid move isn't staying in place
            return True
        return False

    def get_game_state(self):
        return self._game_state

    def is_in_check(self,team):
        if(team == 'red'):
            return self._check_red
        if(team == 'black'):
            return self._check_black


    def check_for_checkmate(self, team):
        '''if a team is in put in check, this method will also be called.
        It expands on the check_for_check method by copying the board to a test board, moving a piece then calling the check for check method'''
        tempboard = self.deepcopy(self._board) # keep a copy of the board and try different moves
        for row in tempboard:
            for piece in row:
                for row_coordinate in range(0,10): #might have to come back and fix calls to None
                    for col_coordinate in range(0,9):
                        if(piece is not None and piece.get_team() == team):
                            piece.move(row_coordinate,col_coordinate,tempboard)
                            if(not self.check_for_check(team,tempboard)):
                                return False
                            else:
                                tempboard = self.deepcopy(self._board)
                            #reset to real board
        return True




class Chariot(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if(symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def move(self,row_coord_to,col_coord_to,board):
        if(self._row == row_coord_to and (not self._col == col_coord_to)): #row is the same, so moving horizontally (across columns)
            if(col_coord_to>self._col): #if moving right
                for x in range(self._col+1, col_coord_to): #this loop checks that the path between the initial and final pos is empty
                    if(board[self._row][x] is not None):
                        return False
                if (board[self._row][col_coord_to] is None or (not board[self._row][col_coord_to].get_team() == self._team)):
                    board[self._row][col_coord_to] = Chariot(self._row,col_coord_to,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there
            else: #moving left, step =-1, checking from one to the left of destination all the way to the one to the right of current pos
                for x in range(self._col-1, col_coord_to,-1): #this loop checks that the path between the initial and final pos is empty
                    if(board[self._row][x] is not None):
                        return False
                if (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
                    board[row_coord_to][col_coord_to] = Chariot(row_coord_to,col_coord_to,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there

        if(self._col == col_coord_to and (not self._row == row_coord_to)): #col is the same, so moving vertically (down/up rows)
            if(self._row<row_coord_to): #moving down the board, row increasing
                for y in range(self._row+1, row_coord_to): #this loop checks that the path between the initial and final pos is empty
                    if(board[y][self._col] is not None):
                        return False
                if (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
                    board[row_coord_to][col_coord_to] = Chariot(row_coord_to,col_coord_to,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there
            else: #moving up the board, so row decreasing, step = -1 as we iterate from bottom to top of a column
                for y in range(row_coord_to+1, self._row,-1): #this loop checks that the path between the initial and final pos is empty
                    if(board[y][self._col] is not None):
                        return False
                if (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
                    board[row_coord_to][col_coord_to] = Chariot(row_coord_to,col_coord_to,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there
        return False #if it's a diagonal move or same coordinate this will trigger

    def __str__(self):
        return self.get_symbol()

class General(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if (symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def __str__(self):
        return self.get_symbol()

    def move(self,row_coord_to,col_coord_to,board):
        if(board[row_coord_to][col_coord_to] is not None):
            if(board[row_coord_to][col_coord_to].get_symbol == 'G' and self._symbol == 'g' and col_coord_to == self._col): #this is the red general flying to black (up the board, row decreasing)
                for row in range(self._row,row_coord_to,-1):
                    if board[row][col_coord_to] is not None:
                        return False
            if (board[row_coord_to][col_coord_to].get_symbol == 'g' and self._symbol == 'G' and col_coord_to == self._col):  # this is the black general flying to red (down the board, row increasing)
                for row in range(self._row, row_coord_to):
                    if board[row][col_coord_to] is not None:
                        return False
        if(col_coord_to >= 3 and col_coord_to <= 5):  # check if moving inside palace
            if (0 <= row_coord_to <= 2 and self._team == 'black'):
                if((col_coord_to==self._col and abs(row_coord_to-self._row)==1) or (row_coord_to==self._row and abs(col_coord_to-self._col)==1)): #moving vertical or horizontal one spot check
                    if(board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team()==self._team)):
                        board[self._row][self._col] = None
                        board[row_coord_to][col_coord_to] = General(row_coord_to, col_coord_to, self._symbol)
                        return True
            elif(9 >= row_coord_to >= 7 and self._team == 'red'):
                if ((col_coord_to == self._col and abs(row_coord_to - self._row) == 1) or (row_coord_to == self._row and abs(col_coord_to - self._col) == 1)):  # moving vertical or horizontal one spot check
                    if (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
                        board[self._row][self._col] = None
                        board[row_coord_to][col_coord_to] = General(row_coord_to,col_coord_to,self._symbol)
                        return True
        return False

class Advisor(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if (symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def __str__(self):
        return self.get_symbol()

    def move(self,row_coord_to,col_coord_to,board):
        if (col_coord_to >= 3 and col_coord_to <= 5):  # check if moving inside palace
            if (0 <= row_coord_to <= 2 and self._team == 'black'):
                if(abs(col_coord_to-self._col) == 1 and abs(row_coord_to-self._row) == 1 and (board[row_coord_to][col_coord_to] is None or board[row_coord_to][col_coord_to].get_team() == 'red' )):
                    board[row_coord_to][col_coord_to] = Advisor(row_coord_to,col_coord_to,self._symbol)
                    board[self._row][self._col] = None
                    return True
            elif (9 >= row_coord_to >= 7 and self._team == 'red'):
                if (abs(col_coord_to - self._col) == 1 and abs(row_coord_to - self._row) == 1 and (board[row_coord_to][col_coord_to] is None or board[row_coord_to][col_coord_to].get_team() == 'black' )):
                    board[row_coord_to][col_coord_to] = Advisor(row_coord_to, col_coord_to, self._symbol)
                    board[self._row][self._col] = None
                    return True
        return False

class Elephant(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if (symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def __str__(self):
        return self.get_symbol()

    def move(self,row_coord_to,col_coord_to,board):
        if(row_coord_to>4 and self._team == 'black'): #river not allowed
            return False
        if(row_coord_to<5 and self._team == 'red'): #river not allowed
            return False
        if (abs(col_coord_to - self._col) == 2 and abs(row_coord_to - self._row) == 2) and (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
            board[row_coord_to][col_coord_to] = Elephant(row_coord_to, col_coord_to, self._symbol) #if statement makes sure that the move is diagonal two spots, and that the spot is either an enemy or empty
            board[self._row][self._col] = None
            return True
        return False

class Horse(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if (symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def __str__(self):
        return self.get_symbol()

    def move(self,row_coord_to,col_coord_to,board):
        if(self._row-row_coord_to == 2 and abs(self._col-col_coord_to) ==1) : #moving vertical up first
            if(board[self._row-1][self._col] is None): #one above start has to be empty or else move is blocked
                if(board[row_coord_to][col_coord_to] is None or not(board[row_coord_to][col_coord_to].get_team() == self._team)): #if final pos empty or enemy
                    board[row_coord_to][col_coord_to] = Horse(row_coord_to,col_coord_to,self._symbol)
                    board[self._row][self._col] = None
                    return True
            return False
        elif(self._row - row_coord_to == -2 and abs(self._col - col_coord_to) == 1):
            # moving vertical down first
            if (board[self._row + 1][self._col] is None):  # one above start has to be empty or else move is blocked
                if (board[row_coord_to][col_coord_to] is None or not (board[row_coord_to][col_coord_to].get_team() == self._team)):  # if final pos empty or enemy
                    board[row_coord_to][col_coord_to] = Horse(row_coord_to, col_coord_to, self._symbol)
                    board[self._row][self._col] = None
                    return True
            return False
        elif (self._col - col_coord_to == 2 and abs(self._row - row_coord_to) == 1):  # moving horizontal left first
            if (board[self._row][self._col-1] is None):  # one to left of start has to be empty or else move is blocked
                if (board[row_coord_to][col_coord_to] is None or not (board[row_coord_to][col_coord_to].get_team() == self._team)):  # if final pos empty or enemy
                    board[row_coord_to][col_coord_to] = Horse(row_coord_to, col_coord_to, self._symbol)
                    board[self._row][self._col] = None
                    return True
            return False
        elif (self._col - col_coord_to == -2 and abs(self._row - row_coord_to) == 1):  # moving horizontal right first
            if (board[self._row][self._col+1] is None):  # one to left of start has to be empty or else move is blocked
                if (board[row_coord_to][col_coord_to] is None or not (board[row_coord_to][col_coord_to].get_team() == self._team)):  # if final pos empty or enemy
                    board[row_coord_to][col_coord_to] = Horse(row_coord_to, col_coord_to, self._symbol)
                    board[self._row][self._col] = None
                    return True
        return False

class Cannon(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if (symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def __str__(self):
        return self.get_symbol()

    def move(self,row_coord_to,col_coord_to,board):
        if(board[row_coord_to][col_coord_to] is None): #the first part checks to see if the move is not a capture; then, it can use the Chariot move to save time and replace the piece at the end
            fakeChariot = Chariot(self._row,self._col,'N')
            if(fakeChariot.move(row_coord_to,col_coord_to,board)):
                board[row_coord_to][col_coord_to] = Cannon(row_coord_to,col_coord_to,self._symbol)
                board[self._row][self._col] = None
                return True
            else:
                return False
        count = 0
        if(self._row == row_coord_to and (not self._col == col_coord_to)): #row is the same, so moving horizontally (across columns)
            if(col_coord_to>self._col): #if moving right
                for x in range(self._col+1, col_coord_to): #this loop checks that the path between the initial and final pos only has one piece to jump
                    if(board[self._row][x] is not None):
                        count+=1
                        if(count>1):
                            return False
                if(count == 0):
                    return False
                if (not board[self._row][col_coord_to].get_team() == self._team): #capture
                    board[self._row][col_coord_to] = Cannon(self._row,col_coord_to,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there
            else: #moving left, step =-1, checking from one to the left of destination all the way to the one to the right of current pos
                for x in range(self._col-1, col_coord_to,-1): #this loop checks that the path between the initial and final pos only has one piece to jump
                    if(board[self._row][x] is not None):
                        count += 1
                        if (count > 1):
                            return False
                if (count == 0): #no pieces
                    return False
                if (not board[row_coord_to][col_coord_to].get_team() == self._team):
                    board[row_coord_to][col_coord_to] = Cannon(self._row,col_coord_to,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there

        if(self._col == col_coord_to and (not self._row == row_coord_to)): #col is the same, so moving vertically (down/up rows)
            if(self._row<row_coord_to): #moving down the board, row increasing as we go from top to bottown
                for y in range(self._row, row_coord_to): #this loop checks that the path between the initial and final pos only has one piece to jump
                    if(board[y][self._col] is not None):
                        count += 1
                        if (count > 1):
                            return False
                        if (count == 0):  # no pieces
                            return False
                if (not board[row_coord_to][col_coord_to].get_team() == self._team):
                    board[row_coord_to][col_coord_to] = Cannon(row_coord_to,self._col,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there
            else: #moving up the board, so row decreasing, step = -1 as we iterate from bottom to top of a column
                for y in range(self._row, row_coord_to,-1): #this loop checks that the path between the initial and final pos only has one piece to jump
                    if(board[y][self._col] is not None):
                        count += 1
                        if (count > 1):
                            return False
                        if (count == 0):  # no pieces
                            return False
                if (not board[row_coord_to][col_coord_to].get_team() == self._team):
                    board[row_coord_to][self._col] = Cannon(row_coord_to,self._col,self._symbol) #check if spot is empty or enemy, move
                    board[self._row][self._col] = None
                    return True
                return False #if friendly piece there, can't move there
        return False #if it's a diagonal move or same coordinate this will trigger

class Soldier(XiangqiGame):
    def __init__(self, row, col, symbol):
        self._row = row
        self._col = col
        self._symbol = symbol
        if (symbol.isupper()):
            self._team = 'black'
        else:
            self._team = 'red'

    def get_symbol(self):
        return self._symbol

    def get_team(self):
        return self._team

    def get_pos(self):
        return [self._row,self._col]

    def __str__(self):
        return self.get_symbol()

    def move(self,row_coord_to,col_coord_to,board):
        if (self._row >4 and self._team == 'black') or (self._row<5 and self._team == 'red'): #crossed river, can move left, right, or forward
            if (row_coord_to == self._row and abs(col_coord_to - self._col) == 1): # horizontal one spot check
                if (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
                    board[row_coord_to][col_coord_to] = Soldier(row_coord_to,col_coord_to,self._symbol)
                    board[self._row][self._col] = None
                    return True

        if col_coord_to == self._col and ((self._row-row_coord_to == 1 and self._team == 'red') or (self._row-row_coord_to== -1 and self._team == 'black')): #vertical moves
            if (board[row_coord_to][col_coord_to] is None or (not board[row_coord_to][col_coord_to].get_team() == self._team)):
                board[row_coord_to][col_coord_to] = Soldier(row_coord_to, col_coord_to, self._symbol)
                board[self._row][self._col] = None
                return True
        return False




# game = XiangqiGame()
# print(game.make_move('b3','e3'))
# game.print()
# print(game.make_move('b8','b3'))
# print(game.make_move('e3','e7'))
# game.print()
#
#










# print(game.make_move('b3', 'b10'))
# game.print()
# print(game.make_move('a10', 'b10'))
# game.print()
# print(game.make_move('b1', 'a3'))
# game.print()
# print(game.make_move('b8', 'c8'))
# print(game.make_move('a4', 'a5'))
# print(game.make_move('h10', 'g8'))
# print(game.make_move('i4', 'i5'))
# print(game.make_move('b10', 'b2'))
# print(game.make_move('a5', 'a6'))
# print(game.make_move('b2', 'h2'))
# print(game.make_move('c1', 'e3'))
# print(game.make_move('h2', 'h3'))
# game.print()
# print(game.make_move('d1', 'e2')) #advisor
# print(game.make_move('h8', 'h1'))
# game.print()
# print(game.make_move('a6', 'b6'))
# print(game.make_move('c8', 'a8'))
# print(game.make_move('b6', 'a6'))
# print(game.make_move('a7', 'a6'))
# print(game.make_move('a3', 'c2'))
# print(game.make_move('a8', 'a1'))
# print(game.make_move('i5', 'i6')) #red soldier crossing river
# game.print()
# print(game.make_move('a1','a2'))
# print(game.make_move('i6', 'i7'))
# print(game.make_move('i10', 'i7'))
# print(game.make_move('e3', 'c5'))
# print(game.make_move('i7', 'i1'))
# print(game.make_move('e2', 'd3'))
# print(game.make_move('h3', 'd3'))
# print(game.make_move('e4', 'e5'))
# print(game.make_move('d3', 'd2'))
# print(game.make_move('g4', 'g5'))
# game.print()
# print(game.make_move('d2', 'e2')) #check i think
# game.print()
# print('is red in check?')
# print(game.is_in_check('red'))
# print(game.make_move('e1', 'd1'))
# print(game.make_move('i1', 'i9'))
# print(game.make_move('c2', 'e3'))
# print('is red in check?')
# print(game.is_in_check('red'))
# print(game.make_move('i9', 'd9')) #check again
# print('is red in check?')
# print(game.is_in_check('red'))
# print(game.make_move('e3', 'd5'))
# game.print()
# print(game.make_move('d9', 'd5')) #checkmate!









