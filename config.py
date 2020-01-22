from colorama import Fore, Back, Style
from board import *
from person import *
from help_input import *
from obstracle import *
import time
import sys
# import board
# import person
# import obstracle
# import help_input

class System(Board, Din, Coins, Fire_Beams, Power_booster, Magnet):
    def __init__(self):
        self.score = 0
        self.board = Board()
        self.fire_beams = Fire_Beams(0, 0, self.board)
        self.power = Power_booster(0,0, self.board)
        self.din = Din(0, 33, 5, self.board)
        self.coins = Coins(0, 0 , self.board)
        self.magnet = Magnet(330, 2, self.board)
        
    def run(self):
        self.board.create_scenery(self.din)
        self.magnet.put_magnet(self.board)
        self.board.move_screen(self.din)
        self.din.move_right(self.board)
        
        self.din.create_din(self.board)
         ##to make sure din does not go out of the screen
    ##    self.board.render(self)
    
    def check_collision(self):
        x = False

        for i in range(10):
            for j in range(10):
                if self.board.grid[self.din.top+i][self.din.left + j] == '$':
                    self.din.collect_coin()
                    self.coins.remove_coin(self.din.left + j, self.din.top + i, self.board)
                    
                if self.board.grid[self.din.top+i][self.din.left+j]  == '*':
                    if(self.din.shield_on == 0):
                        self.din.decrease_live(self.board)
                        self.din.speed = 1
                        self.din.boost_time = 0
                        self.board.left = 0
                        self.din.remove_din_on_collision(self.board)
                        self.din.left = 0
                        self.din.top = 33
                        self.fire_beams.put_beams(obj_system.board)
                    else:
                        self.din.enemy_killed_increase()
                        self.fire_beams.remove_beam(self.din.left, self.board)

                    x = True
                
                if self.board.grid[self.din.top+i][self.din.left+j] == '@':
                    self.board.grid[self.din.top+i][self.din.left+j]= ' ' 
                    self.din.boost_time = self.din.boost_time + 1
                    self.din.speed = 2  
                    
                    # self.fire_beams.remove_beam(self.din.left, self.board)
                    # self.din.remove_din(self.board)
                    # self.din.left = self.board.left
                    # self.din.top = self.board.height-17
                    
        # if coin == True:
            
        return x
        
    def render(self):
        for i in range(self.board.height - 8):
            for j in range(self.board.left, self.board.left + self.board.s_width):
                # print(Back.GREEN + self.board.grid[i][j], end='')
                if(self.board.grid[i][j] == '(' or self.board.grid[i][j] == ')'):
                    print(Fore.WHITE + self.board.grid[i][j] + Fore.RESET, end='')
                    #print(Style.RESET_ALL)
                elif(self.board.grid[i][j] == '*'):
                    print(Fore.RED + self.board.grid[i][j] + Fore.RESET, end='')
                    # print(Style.RESET_ALL)
                elif(self.board.grid[i][j] == '@'):
                    print(Fore.BLACK + self.board.grid[i][j] + Fore.RESET, end='')
                elif(self.board.grid[i][j] == '-'):
                    print(Fore.WHITE +self.board.grid[i][j] + Fore.RESET, end='')
                    # print(Style.RESET_ALL)
                elif(self.board.grid[i][j] == '$'):
                    print(Fore.YELLOW + self.board.grid[i][j] + Fore.RESET, end='')
                    # print(Style.RESET_ALL)
                elif(self.board.grid[i][j] == '|'):
                    print(Fore.CYAN + self.board.grid[i][j] + Fore.RESET, end='')
                elif(self.board.grid[i][j] == 'o'):
                    print(Fore.MAGENTA + self.board.grid[i][j] + Fore.RESET, end='')
                else:
                    print(Back.BLUE + self.board.grid[i][j], end='')
                    # print(Style.RESET_ALL)
                # print(Fore.RESET)
                # elif(self.board.grid[i][j] == '.'):
                #     print(Fore.RED + self.board.grid[i][j], end=' ')
                # print(Back.GREEN)
            print()
            # print(Style.RESET_ALL)
   
        for i in range(self.board.height - 8, self.board.height):
            for j in range(self.board.s_width):
                # print(Back.GREEN + self.board.grid[i][j], end='')
                
                print(Back.GREEN + self.board.grid[i][j] , end='')
                
                # print(Back.GREEN)
            print()
            # print(Style.RESET_ALL)
            # print(Style.RESET_ALL)
            
            
            
            
            
            
            
            
            

obj_system = System()
# obj_system.run()
# obj_system.render()
obj_system.coins.put_coins(obj_system.board)
obj_system.fire_beams.put_beams(obj_system.board)
obj_system.power.create_power_booster(obj_system.board)
obj_system.magnet.put_magnet(obj_system.board)
orig_time = time.time()
x = True
gravity_t = 0

object_yes = 0

#### For shield I have first shield_on in din object, then I have shield_start_time and shield_gap_time and shield_gap_on 
shield_start_time = 0
shield_gap_time = 0
shield_gap_on = 0
magnet_on = 0
co = 0

while(x):
    print('\033[H')
    # print("sheild_start" + str(sheild_start)
    # print("Sheild_gap" + str(sheild_gap))
    # print("Sheild_on" + str(obj_system.din.sheild_on))
    if obj_system.din.left >= 210 and obj_system.din.left <= 335 and magnet_on == 0:   ##move right
        obj_system.din.move_right(obj_system.board)
        magnet_on = 1
        #obj_system.din.move_right(obj_system.board)
    elif obj_system.din.left >= 450 and obj_system.din.left <= 410 and magnet_on == 0:
        obj_system.din.move_left(obj_system.board)
        magnet_on = 1
        #obj_system.din.move_left(obj_system.board)
    elif magnet_on == 1:
        magnet_on = 0
        
    
    
    
    if time.time() - shield_start_time > 10 and obj_system.din.shield_on == 1:
        shield_gap_time = time.time()
        obj_system.din.shield_on = 0
        shield_start_time = 0
        shield_gap_on = 1
        obj_system.din.remove_din(obj_system.board)
        
    if time.time() - shield_gap_time > 15 and shield_gap_on == 1:
        shield_gap_on = 0
        
     
    # if sheild_start == 0 and obj_system.din.sheild_on == 1:
    #     sheild_gap = 60
    #     obj_system.din.sheild_on = 0
        
         
    if(obj_system.din.top < 33):
        gravity_t += 0.2
        acc = round(0.5 * gravity_t * gravity_t)
        obj_system.din.remove_din(obj_system.board)
        if(obj_system.din.top + 8 + acc <= obj_system.board.height - 9):
            obj_system.din.top += acc
        else:
            obj_system.din.top = obj_system.board.height - 9 - 8
    
    # if time.time() - orig_time >= 0.15:
    #     is_collision = obj_system.check_collision()
    #     # obj_system.fire_beams.put_beams(obj_system.board)
    #     obj_system.run()
    #     obj_system.render()
    #     orig_time = time.time()
    #     if obj_system.din.boost_time >= 0.15:
    #         obj_system.din.boost_time -= 0.15
    #     else:
    #         obj_system.din.boost_time = 0
    #         obj_system.din.speed = 1
    
    if time.time() - orig_time >= 0.15:
        is_collision = obj_system.check_collision()
        # obj_system.fire_beams.put_beams(obj_system.board)
        if object_yes == 1: 
            object_yes = 2
        else:
            for i in range(50):
                for j in range(co-200, co + 200):
                    if obj_system.board.grid[i][j] == 'o':
                        obj_system.board.grid[i][j] = ' '
            
            object_yes = 0
        obj_system.run()
        obj_system.render()
        orig_time = time.time()
        if obj_system.din.boost_time >= 0.15:
            obj_system.din.boost_time -= 0.15
        else:
            obj_system.din.boost_time = 0
            obj_system.din.speed = 1
    
    # for i in range(10):
    #     for j in range(10):
    #         if obj_system.board.grid[obj_system.din.top+i][obj_system.din.left+j] == '$':
    #             obj_system.din.collect_coin()
    #             obj_system.coins.remove_coin(obj_system.board)   
    # obj_system.check_collision()
    # obj_system.run()
    # obj_system.render()
    # orig_time = time.time()
    
        
    inp = get_input()
    if inp == 'd':
        is_collision = obj_system.check_collision()
        # if obj_system.din.left >= 260 and obj_system.din.left <= 335:   ##move right
        #     obj_system.din.move_right(obj_system.board)
            
        if is_collision == False:
            obj_system.din.move_right(obj_system.board)
    elif inp == 'a':
        is_collision = obj_system.check_collision()
        # if obj_system.din.left >= 260 and obj_system.din.left <= 335:   ##move right
        #     obj_system.din.move_right(obj_system.board)
        if is_collision == False:
            obj_system.din.move_left(obj_system.board)
    elif inp == 'w':
        gravity_t = 0
        is_collision = obj_system.check_collision()
        if is_collision == False:
            obj_system.din.jump(obj_system.board)
            
    elif inp == 'f': ##fire bullet
        object_yes = 1 
        for i in range(90):
            if obj_system.board.grid[obj_system.din.top +4][obj_system.din.left + 9 + i] == '*':
                co = obj_system.din.left + 9 + i
                obj_system.din.enemy_killed_increase()
                obj_system.fire_beams.remove_beam_only_right(co, obj_system.board)   
        for i in range(30):
            obj_system.board.grid[obj_system.din.top + 4][obj_system.din.left + 9 + i] =  'o'
        # obj_system.render()
        # for i in range(30):
        #     obj_system.board.grid[obj_system.din.top + 4][obj_system.din.left + 9 + i] =  ' '
            
    elif inp == ' ': 
        if obj_system.din.shield_on == 0 and shield_gap_on == 0:
            obj_system.din.shield_on = 1
            shield_start_time = time.time()
            obj_system.din.create_din(obj_system.board)
        
        # if sheild_start == 10 and obj_system.din.sheild_on == 0:
        #     obj_system.din.sheild_on = 1
        #     sheild_start = 10
        #     obj_system.din.create_din(obj_system.board)
        
        
        
    elif inp == 'q':
        quit()
        x = False
    if obj_system.din.lives <= 0:
        os.system('clear')
        obj_system.render()
        print('Game Over')
        print("Score : " , obj_system.din.coins)
        time.sleep(1)
        sys.exit(0)
    # elif inp == 'x':
    #     obj_system.din.move_down(obj_system.board)
    
                

        

