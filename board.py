import time
import os
import random
from colorama import Fore, Back, Style 

class Board:
    def __init__(self):
        self.width = 1400
        self.height = 50
        self.s_width = 200
        self.left = 0
        self.grid = [[' ' for i in range(self.width)] for j in range(self.height)]
        self.coins = []
        self.bullets = []
        self.black = '\u001b[30;1m'
        self.red = '\u001b[31;1m'
        self.green = '\u001b[32;1m'
        self.yellow = '\u001b[33;1m'
        self.blue = '\u001b[34;1m'
        self.magenta = '\u001b[35;1m'
        self.cyan = '\u001b[36;1m'
        self.white = '\u001b[37;1m'
        self.reset = '\u001b[0m'
    
    def move_screen(self, din):
        self.left = self.left + din.speed
        self.grid[0][self.left+0] = Fore.WHITE + 'C' + Fore.RESET
        self.grid[0][self.left+1] = Fore.WHITE + 'O' + Fore.RESET
        self.grid[0][self.left+2] = Fore.WHITE + 'I' + Fore.RESET
        self.grid[0][self.left+3] = Fore.WHITE + 'N' + Fore.RESET
        self.grid[0][self.left+4] = Fore.WHITE + 'S' + Fore.RESET
        self.grid[0][self.left+5] = Fore.WHITE + '-' + Fore.RESET
        self.grid[0][self.left+7] =  Fore.WHITE + str(din.coins % 10) + Fore.RESET 
        self.grid[0][self.left+6] = Fore.WHITE + str(din.coins // 10) + Fore.RESET 
        self.grid[0][self.left+8] = Fore.WHITE + ' ' + Fore.RESET
        self.grid[0][self.left+9] = Fore.WHITE + 'L' + Fore.RESET
        self.grid[0][self.left+10] = Fore.WHITE + 'I' + Fore.RESET
        self.grid[0][self.left+11] = Fore.WHITE + 'V' + Fore.RESET
        self.grid[0][self.left+12] = Fore.WHITE + 'E' + Fore.RESET
        self.grid[0][self.left+13] = Fore.WHITE + 'S' + Fore.RESET
        self.grid[0][self.left+14] = Fore.WHITE + str(din.lives) + Fore.RESET 

    def create_boundary(self, din):
        
        for i in range(self.width):
            # self.grid[self.height - 1][i] = Fore.WHITE + '^' + Fore.RESET
            self.grid[self.height - 1][i] = '^'
        ### making sky above which the mad can't go
        for i in range(self.width):
            self.grid[0][i] = Fore.WHITE + '-' + Fore.RESET 
        # self.grid[0][0] = 'C'
        # self.grid[0][1] = 'O'
        # self.grid[0][2] = 'I'
        # self.grid[0][3] = 'N'
        # self.grid[0][4] = 'S'
        # self.grid[0][6] =  str(din.coins % 10)
        # self.grid[0][5] = str(din.coins // 10)
           
    
    def create_clouds(self, left, top):
        self.grid[top+3][left] = '('
        self.grid[top+3][left+1] = '('
        self.grid[top+3][left+2] = '('
        self.grid[top+3][left+3] = ')'
        self.grid[top+3][left+4] = ')'
        self.grid[top+3][left+5] = ')'
        self.grid[top+2][left+1] = '('
        self.grid[top+2][left+2] = '('
        self.grid[top+2][left+3] = ')'
        self.grid[top+2][left+4] = ')'
        self.grid[top+1][left+2] = '('
        self.grid[top+1][left+3] = ')'

    # def create_coins(self, left, top):
    #     number = random.randrange(1,10)
    #     for i in range(number):
    #         self.grid[top][left+i] = '$'
    #         self.grid[top+1][left+i] = '$'
        
    def create_scenery(self, din):
        self.create_boundary(din)
        ######## Creating clouds ########
        self.create_clouds(50, 14)
        self.create_clouds(100, 6)
        self.create_clouds(150, 15)
        self.create_clouds(200, 17)
        self.create_clouds(250, 13)
        self.create_clouds(300, 15)
        self.create_clouds(350, 6)
        self.create_clouds(400, 14)    
        self.create_clouds(450, 14)
        self.create_clouds(550, 6)
        self.create_clouds(600, 15)
        self.create_clouds(730, 17)
        self.create_clouds(760, 13)
        self.create_clouds(800, 15)
        self.create_clouds(900, 6)
        self.create_clouds(1000, 14)
        self.create_clouds(1050, 14)
        self.create_clouds(1101, 6)
        self.create_clouds(1140, 15)
        self.create_clouds(1200, 17)
        self.create_clouds(1250, 13)
        self.create_clouds(1300, 15)
        self.create_clouds(1350, 6)
         
        #### Putting coins ######
        # for i in range(0, 1200, 200):
            
        #     x = random.randint(13, 30) ##height
        #     y = random.randint(5, 150)  ##width
        #     self.create_coins(y+i, x)
            
        
            

