## Logical Operators
# Problem Input

Write a program that allows to ride on roller coaster above height 120 cm. differentiate ticket fare by age group using logical operators. also ask do they want to take photo while riding?

# Example Input 1

```
6
Do you want photo taken? Y or N :
Y
```

# Example Output 1

```
Please pay ₹150.
```

# Example Input 2

```
15
Do you want photo taken? Y or N :
N
```

# Example Output 2

```
Please pay ₹90.
```

# Problem Output
```
print("Welcome to jubly RollerCoster!")
height = int(input("What is your height in cm?\n "))
bill = 0
if height >= 120:
    print("You can ride on RollerCoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 50
        print("Please pay ₹50.")
    elif age >= 12 and age <=18:
        bill = 90
        print("Please pay ₹90.")
    elif age >= 45 and age <=55:
        bill = 0
        print("Your Ride is FREE.")
    else:
        bill = 120
        print("Please pay ₹120.")
    want_photo = input("Do you want photo taken? Y or N : ")
    if want_photo == "Y":
        bill += 1005
    print(f"Please pay ₹{bill}")
else:
    print("Sorry, You have to grow taller before you can Ride.")
```