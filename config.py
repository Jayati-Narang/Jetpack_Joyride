from colorama import Fore, Back, Style
from board import *
from person import *
from help_input import *
from obstracle import *
# import board
# import person
# import obstracle
# import help_input

class System(Board, Din, Coins):
    def __init__(self):
        self.score = 0
        self.board = Board()
        self.din = Din(0, 33, 5, self.board)
        self.coins = Coins(0, 0 , self.board)
        
    def run(self):
        self.board.create_scenery(self.din)
        self.board.move_screen(self.din)
        self.din.move_right(self.board)
        
        self.din.create_din(self.board)
         ##to make sure din does not go out of the screen
    ##    self.board.render(self)
    
    def check_collision(self):
        for i in range(9):
            for j in range(9):
                if self.board.grid[self.din.top+i][self.din.left + j] == '$':
                    self.din.collect_coin()
                    self.coins.remove_coin(self.board)
        
    def render(self):
        for i in range(self.board.height - 8):
            for j in range(self.board.left, self.board.left + self.board.s_width):
                # print(Back.GREEN + self.board.grid[i][j], end='')
                if(self.board.grid[i][j] == '(' or self.board.grid[i][j] == ')'):
                    print(Fore.WHITE + self.board.grid[i][j], end='')
                elif(self.board.grid[i][j] == '-'):
                    print(Fore.WHITE +self.board.grid[i][j], end='')
                elif(self.board.grid[i][j] == '$'):
                    print(Fore.YELLOW + self.board.grid[i][j], end='')
                else:
                    print(Back.BLUE + self.board.grid[i][j], end='')
                # print(Style.RESET_ALL)
                # elif(self.board.grid[i][j] == '.'):
                #     print(Fore.RED + self.board.grid[i][j], end=' ')
                # print(Back.GREEN)
            print()
            # print(Style.RESET_ALL)
        for i in range(self.board.height - 8, self.board.height):
            for j in range(self.board.s_width):
                # print(Back.GREEN + self.board.grid[i][j], end='')
                print(Back.GREEN + self.board.grid[i][j], end='')
                
                # print(Back.GREEN)
            print()
            # print(Style.RESET_ALL)

obj_system = System()
# obj_system.run()
# obj_system.render()
obj_system.coins.put_coins(obj_system.board)

while(True):
    print('\033[H')
    # for i in range(10):
    #     for j in range(10):
    #         if obj_system.board.grid[obj_system.din.top+i][obj_system.din.left+j] == '$':
    #             obj_system.din.collect_coin()
    #             obj_system.coins.remove_coin(obj_system.board)   
    obj_system.check_collision()
    obj_system.run()
    obj_system.render()

    inp = get_input()
    if inp == 'd':
        obj_system.din.move_right(obj_system.board)
    elif inp == 'a':
        obj_system.din.move_left(obj_system.board)
    elif inp == 'w':
        obj_system.din.jump(obj_system.board)
    # elif inp == 'x':
    #     obj_system.din.move_down(obj_system.board)
    
                

        

