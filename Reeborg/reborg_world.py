def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_up():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def go_down():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

    
def jump_the_hurdle():
    go_up()
    move()
    go_down()
    
 
def move_carefully():
    if not front_is_clear():
        jump_the_hurdle()
    else:
        move()
    
while not at_goal():
    move_carefully()
    
