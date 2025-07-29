print("Welcome to Python Pizza deliveries!")
size_first_input = input("What size pizza do you want? S, M or L: ")
size = size_first_input.upper()
pepperoni = input("Do want pepperoni on your pizza? Y or N: ")
pep = pepperoni.upper()
extra_cheese = input("Do you extra cheese? Y or N?")
cheese = extra_cheese.upper()

bill = 0
# Calculate for bill for the size of pizza
if (size == "S"):
    bill += 15
elif (size == "M"):
    bill += 20
elif (size == "L"):
    bill += 25
else:
    print("You didn't enter the correct input")

# calculate bill for pepperoni for small and large or medium

if (pep == "Y"):
    if (size == "S"):
        bill += 2
    else:
        bill += 3

# calculate bill with extra cheese

if (cheese == "Y"):
    bill += 1 

print(f"Your final bill is: ${bill}")
 
