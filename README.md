# OBJECTIVE
The objective of the game is to save Din by killing Boss enemy before times up after 700 sec

# RUNNING THE GAME
```
python3 config.py

```

# FEATURES
- The game is implemented in Python3
- Uses only core Python3 packages
- Player can move right, left and jump 
- Player loses live if collide with Fire beams(red color '*') 
- Player can use shield to protect it from fire beams 
- On collecting power booster '@' player's speed boosts up so as the screen moves faster 
- Colors are implemented
- Gravity is implemented
- Boss enemy is also implemented

# MOVEMENT
- a - Move Backwards
- d - Move forward
- w - Jump vertical 
- space key - Shield activates for 10 sec 
- f - To fire bullet

# OOP
- #### Inheritance
    - Player and Enemy class inherit from the Person class
- #### Polymorphism
   - The jump function in each of the child classes of the Person class overrides the jump function of the Person class
- #### Encapsulation
    - Class and object based approach for all the functionality implemented
- #### Abstraction
    - Properties of the board class are hidden from the user using abstraction

# OBSTACLES
- Fire beams are the various obstacles implemented

# BACKGROUND AND SCENERY
- Clouds and sky and ground boundary is implemented

# BOSS ENEMY
- Boss enemy adjusts its position according to the player
- It has 3 lives
- It also fires bullets

# TIME LIMIT
- Time limit of the game is 700 sec

# SCORE
- The final score is calculated as:
```
score = 2 * (number of enemies killed) + 1 * (number of coins collected)
```
