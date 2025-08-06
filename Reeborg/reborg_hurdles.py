# function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# function to go up
def go_up():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

# function to go down
def go_down():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# function to go jump the hurdle   
def jump_the_hurdle():
    go_up()
    move()
    go_down()
    
# function to go move through the hurdle   
def move_carefully():
    if not front_is_clear():
        jump_the_hurdle()
    else:
        move()
    
while not at_goal():
    move_carefully()
    
