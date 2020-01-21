import random
# class Obstacle:
#     def __init__(self, left, top):
#         self.left = left
#         self.top = top
class Coins:
    def __init__(self, left, top, board):
        self.left = left
        self.top = top
    
    def create_coins(self, left, top, board):
        number = random.randrange(1,10)
        for i in range(number):
            board.grid[top][left+i] = '$'
            # board.grid[top+1][left+i] = '$'
    
    def put_coins(self, board):
        for i in range(0, 1200, 200):
            
            x = random.randint(13, 30) ##height
            y = random.randint(5, 150)  ##width
            self.create_coins(y+i, x, board)
    
    def remove_coin(self, board):
        board.grid[self.top][self.left] = ' '