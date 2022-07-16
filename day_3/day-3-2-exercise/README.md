
## Nested If - elif
# Problem Input

Write a program that allows to ride on roller coaster above height 120 cm. differentiate ticket fare by age groups.

# Example Input 1

```
6
```

# Example Output 1

```
Please pay ₹50.
```

# Example Input 2

```
15
```

# Example Output 2

```
Please pay ₹90.
```
# Example Input 3

```
35
```

# Example Output 3

```
Please pay ₹120.
```

# Problem Output
```
print("Welcome to jubly RollerCoster!")
height = int(input("What is your height in cm?\n "))
if height >= 120:
    print("You can ride on RollerCoster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay ₹50.")
    elif age <= 12 or age >=18:
        print("Please pay ₹90.")    
    else:
        print("Please pay ₹120.")    
else:
    print("Sorry, You have to grow taller before you can Ride.")
```