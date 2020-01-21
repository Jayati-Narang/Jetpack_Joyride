import random
# class Obstacle:
#     def __init__(self, left, top, board):
#         self.left = left
#         self.top = top
class Coins:
    def __init__(self, left, top, board):
        self.left = left
        self.top = top
        # super().__init__(left, top, board)
        
    
    def create_coins(self, left, top, board):
        number = random.randrange(1,10)
        for i in range(number):
            board.grid[top][left+i] = '$'
            board.grid[top+1][left+i] = '$'
    
    def put_coins(self, board):
        for i in range(0, 1200, 200):
            
            x = random.randint(13, 30) ##height
            y = random.randint(5, 150)  ##width
            self.create_coins(y+i, x, board)
    
    def remove_coin(self, board):
        board.grid[self.top][self.left] = ' '
    
    
class Fire_Beams:
    def __init__(self, left, top, board):
        self.left = left
        self.top = top
    def create_horizontal_beams(self, left, top, board):
        for i in range(6):
            board.grid[top][left + i] = '*'
    def create_vertical_beams(self, left,top, board):                              
        for i in range(6):                                    
            board.grid[top+i][left] = '*'                             
    def create_slanting_beams(self, left, top, board):                                                
        for i in range(6):                                        
            board.grid[top+5-i] [left + i] = '*'

    def put_beams(self,board):
        # for i in range(0, 1200, 75):
        #     self.create_horizontal_beams(0 + i, 12, board)
        #     self.create_vertical_beams(89 + i, 24, board)
        #     self.create_slanting_beams(47+ i, 34, board)
       
        self.create_horizontal_beams(30, 34, board)
        self.create_vertical_beams(60, 24, board)
        self.create_slanting_beams(90, 12, board)
        self.create_horizontal_beams(120, 31, board)
        self.create_vertical_beams(150, 22, board)
        self.create_slanting_beams(182, 11, board)
        self.create_horizontal_beams(210, 34, board)
        self.create_vertical_beams(240, 24, board)
        self.create_slanting_beams(270, 12, board)
        self.create_horizontal_beams(300, 34, board)
        self.create_vertical_beams(330, 24, board)
        self.create_slanting_beams(360, 12, board)
        self.create_horizontal_beams(390, 34, board)
        self.create_vertical_beams(420, 24, board)
        self.create_slanting_beams(450, 12, board)
        self.create_horizontal_beams(480, 34, board)
        self.create_vertical_beams(510, 24, board)
        self.create_slanting_beams(540, 12, board)
        self.create_horizontal_beams(570, 34, board)
        self.create_vertical_beams(600, 24, board)
       
        self.create_horizontal_beams(630, 34, board)
        self.create_vertical_beams(660, 24, board)
        self.create_slanting_beams(690, 12, board)
        self.create_horizontal_beams(720, 34, board)
        self.create_vertical_beams(750, 24, board)
        self.create_slanting_beams(780, 12, board)
        self.create_horizontal_beams(810, 34, board)
        self.create_vertical_beams(840, 24, board)
        self.create_slanting_beams(870, 12, board)
        self.create_horizontal_beams(900, 34, board)
        self.create_vertical_beams(930, 24, board)
        self.create_slanting_beams(960, 12, board)
        self.create_horizontal_beams(990, 34, board)
        self.create_vertical_beams(1020, 24, board)
        self.create_slanting_beams(1080, 12, board)
        self.create_horizontal_beams(1120, 34, board)
        self.create_vertical_beams(1160, 24, board)
        self.create_slanting_beams(1200, 12, board)
        self.create_horizontal_beams(1250, 34, board)
        self.create_vertical_beams(1280, 24, board)
        self.create_slanting_beams(1310, 12, board)
                    

        