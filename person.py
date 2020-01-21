import time

class Person:
    def __init__(self, left, top, lives, board):
      self.left = left
      self.top = top
      self.coins = 0
      
class  Din(Person):
    def __init__(self, left, top, lives, board):
        super().__init__(left, top, lives, board)
        self.s_time = round(time.time())
    def create_din(self, board):
        board.grid[self.top][self.left+4] = '.'
        board.grid[self.top+1][self.left+3] = '.'
        board.grid[self.top+1][self.left+5] = '.'
        # board.grid[self.top+2][self.left+2] = '.'
        # board.grid[self.top+2][self.left+3] = '.'
        # board.grid[self.top+2][self.left+4] = '.'
        # board.grid[self.top+2][self.left+5] = '.'
        # board.grid[self.top+2][self.left+6] = '.'
        for i in range(2,6):
            for j in range(2, 7):
                board.grid[self.top+i][self.left+j] = '.'
        for i in range(6, 9):
            board.grid[self.top+i][self.left+3] = '.'
            board.grid[self.top+i][self.left+5] = '.'
        board.grid[self.top+3][self.left+1] = '.'
        board.grid[self.top+4][self.left] = '.'
        board.grid[self.top+3][self.left+7] = '.'
        board.grid[self.top+4][self.left+8] = '.'
                        
        # for i in range(2):
        #     for j in range (2):
        #         board.grid[self.top+i][self.left+j] = 'm'
                
    def remove_din(self, board):
        board.grid[self.top][self.left+4] = ' '
        board.grid[self.top+1][self.left+3] = ' '
        board.grid[self.top+1][self.left+5] = ' '
        # board.grid[self.top+2][self.left+2] = '.'
        # board.grid[self.top+2][self.left+3] = '.'
        # board.grid[self.top+2][self.left+4] = '.'
        # board.grid[self.top+2][self.left+5] = '.'
        # board.grid[self.top+2][self.left+6] = '.'
        for i in range(2,6):
            for j in range(2, 7):
                board.grid[self.top+i][self.left+j] = ' '
        for i in range(6, 9):
            board.grid[self.top+i][self.left+3] = ' '
            board.grid[self.top+i][self.left+5] = ' '
        board.grid[self.top+3][self.left+1] = ' '
        board.grid[self.top+4][self.left] = ' '
        board.grid[self.top+3][self.left+7] = ' '
        board.grid[self.top+4][self.left+8] = ' '
## The screen will move continuously therefore when mario reaches the border then we have to push mario to right but this condition won't be put here ## 
    def move_left(self, board):
        if self.left > 1 and self.left > board.left - 1:
            self.remove_din(board)
            self.left = self.left - 1
                
    def move_right(self, board):
        if self.left+8 != 1399 and self.left+9 != board.left+200: 
            self.remove_din(board)     
            self.left = self.left + 1
    def jump(self, board):
        if self.top != 0:
            self.remove_din(board)
            self.top = self.top - 1
            
            
        
    # def move_down(self, board):
    #     if self.top + 9 != board.height - 8:
    #         if board.grid[]
    # def move_left(self, board, coins):
    #     if self.left != 0 and self.left != board.left:
    #         t = False
    #         for i in range(9):
    #             for j in range(9):              #########Coins are yet to be considered ######
    #                 # if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                 #     t = True if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                 #     t = True 
    #                 if board.grid[self.top + i][self.left +j] == '$':
    #                     self.collect_coin()
    #                     coins.remove_coin(board)
    #                 elif board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                     t = True 
                        
    #         if t != True: ##then you can move
    #             self.remove_din(board)
    #             self.left = self.left - 1
    
    # def move_right(self, board, coins):
    #     if self.left+8 != 1399 and self.left+9 != board.left+200:
    #         t = False
    #         for i in range(9):
    #             for j in range(9):
    #                 if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                     t = True
    #                 if board.grid[self.top + i][self.left +j] == '$':
    #                     self.collect_coin()
    #                     coins.remove_coin(board)
    #         if t != True:
    #             self.remove_din(board)     
    #             self.left = self.left + 1  
    
    # def jump(self, board, coins):
    #     if self.top != 0:
    #         t = False
    #         for i in range(9):
    #             for j in range(9):
    #                 if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                     t = True
    #                 if board.grid[self.top + i][self.left +j] == '$':
    #                     self.collect_coin()
    #                     coins.remove_coin(board)
    #         if t != True:
    #             self.remove_din(board)     
    #             self.top = self.top - 1  
    
    def collect_coin(self):
        self.coins = self.coins + 1
    
                                                                                                                                                                                                                                                                                                                                                                                            