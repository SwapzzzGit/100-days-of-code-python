print("Welcome to jubly RollerCoster!")
height = int(input("What is your height in cm?\n "))
bill = 0
if height >= 120:
    print("You can ride on RollerCoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 50
        print("Please pay ₹50.")
    elif age >= 12 or age <=18:
        bill = 90
        print("Please pay ₹90.")    
    else:
        bill = 120
        print("Please pay ₹120.")
    want_photo = input("Do you want photo taken? Y or N : ")
    if want_photo == "Y":
        bill += 100
        print(f"Please pay ₹{bill}")
else:
    print("Sorry, You have to grow taller before you can Ride.")