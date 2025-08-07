print("Welcome to the Treasure Island.\nYour Mission is to find the treasure.")

option = input("left or right?")

if option == "left":
    option = input("swim or wait?")
    
    if option == "wait":
        option = input("Which door? red, blue or yellow?")

        if option == "yellow":
            print("You Win!!!")
        elif (option == "red" or option =="blue"):
            print("Game Over!")
        else:
            print("Not a valid response")

    elif option == "swim":
        print("Game Over!")
    else:
        print("Not a valid input!")

elif option == "right":
    print("Game Over!")
else:
    print("Not a valid input!")
