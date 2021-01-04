# xiangqiGame
Fully functioning Xiangqi ("chinese chess") game that pits two players against each other. 
Coded in Python, operating through the command line using traditional chess algebraic coordinates. 
XiangqiGame for playing a board game called xiangqi. 
Please read the "Board", "Rules", and "Pieces" sections on the Wikipedia page.
Perpetual check or chasing rules not applicable here.

Red is the starting player.

Locations on the board are specified using "algebraic notation", with columns labeled a-i and rows labeled 1-10, 
with row 1 being the Red side and row 10 the Black side.

Example of how the game can be played:

game = XiangqiGame()
move_result = game.make_move('c1', 'e3')
black_in_check = game.is_in_check('black')
game.make_move('e7', 'e6')
state = game.get_game_state()
