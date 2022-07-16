print("Welcome to jubly RollerCoster!")
height = int(input("What is your height in cm?\n "))
if height >= 120:
    print("You can ride on RollerCoster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay ₹50.")
    elif age >= 12 or age <=18:
        print("Please pay ₹90.")    
    else:
        print("Please pay ₹120.")    
else:
    print("Sorry, You have to grow taller before you can Ride.")