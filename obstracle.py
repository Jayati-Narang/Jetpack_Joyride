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
    
    def remove_coin(self, left, top, board):
        board.grid[top][left] = ' '
    
    
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
       
        self.create_horizontal_beams(30, 8, board)
        self.create_vertical_beams(60, 24, board)
        self.create_slanting_beams(90, 12, board)
        self.create_horizontal_beams(120, 8, board)
        self.create_vertical_beams(150, 22, board)
        self.create_slanting_beams(182, 11, board)
        self.create_horizontal_beams(210, 8, board)
        self.create_vertical_beams(240, 24, board)
        self.create_slanting_beams(270, 12, board)
        self.create_horizontal_beams(300, 8, board)
        self.create_vertical_beams(330, 24, board)
        self.create_slanting_beams(360, 12, board)
        self.create_horizontal_beams(390, 8, board)
        self.create_vertical_beams(420, 24, board)
        self.create_slanting_beams(450, 12, board)
        self.create_horizontal_beams(480, 8, board)
        self.create_vertical_beams(510, 24, board)
        self.create_slanting_beams(540, 12, board)
        self.create_horizontal_beams(570, 8, board)
        self.create_vertical_beams(600, 24, board)
       
        self.create_horizontal_beams(630, 8, board)
        self.create_vertical_beams(660, 24, board)
        self.create_slanting_beams(690, 12, board)
        self.create_horizontal_beams(720, 8, board)
        self.create_vertical_beams(750, 24, board)
        self.create_slanting_beams(780, 12, board)
        self.create_horizontal_beams(810, 8, board)
        self.create_vertical_beams(840, 24, board)
        self.create_slanting_beams(870, 12, board)
        self.create_horizontal_beams(900, 8, board)
        self.create_vertical_beams(930, 24, board)
        self.create_slanting_beams(960, 12, board)
        self.create_horizontal_beams(990, 8, board)
        self.create_vertical_beams(1020, 24, board)
        self.create_slanting_beams(1080, 12, board)
        self.create_horizontal_beams(1120, 8, board)
        self.create_vertical_beams(1160, 24, board)
        self.create_slanting_beams(1200, 12, board)
        self.create_horizontal_beams(1250, 8, board)
        self.create_vertical_beams(1280, 24, board)
        self.create_slanting_beams(1310, 12, board)
                    

    def remove_beam(self, left, board):
        for  i in range(50):
            for j in range(left - 7, left + 7):
                if board.grid[i][j] == '*':
                    board.grid[i][j] = ' '
            
            
class Power_booster:
    def __init__(self,x,y,board):
        self.x = x
        self.y = y
    
    def create_power_booster(self, board):
        board.grid[20][12] = '@'
        board.grid[23][100]='@'
        board.grid[26][162]='@'
        board.grid[12][202]='@'
        board.grid[4][302]='@'
        board.grid[30][402]='@'
        board.grid[25][503]='@'    
        board.grid[26][543]='@'
        board.grid[27][637]='@'
        board.grid[13][739]='@'
        board.grid[10][803]='@'
        board.grid[31][920]='@'
        board.grid[29][1001]='@'
        board.grid[38][1207]='@'
        board.grid[29][1302]='@'
