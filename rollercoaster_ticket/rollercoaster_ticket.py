# Print a welcome message
print("Welcome to the rollercoaster!")

# collect the height info
height = int(input("What is your height in cm?"))

# declare bill variable
bill = 0

# Check if height is greater and equal to 120
if height>= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))   # Collect age info
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is Free")
    
    else:
        bill=22
        print(f"Adult tickets are ${bill}.")

    wants_photo = input("Do you want a photo takesn? Y or N.") # check if user wants to take a photo 
    if wants_photo =="Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
