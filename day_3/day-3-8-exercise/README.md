## Pizza Order

# Problem Input

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: ₹150
```

```
Medium Pizza: $230
```

```
Large Pizza: ₹349
```

```
Pepperoni for Small Pizza: +₹35
```

```
Pepperoni for Medium or Large Pizza: +₹50
```

```
Extra cheese for any size pizza: + ₹20
```

# Problem Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Problem Output

```
Your final bill is: ₹399.
```
# Solution

```
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
  bill += 150
elif size == "M":
  bill += 230
else:
  bill += 349

if add_pepperoni == "Y":
  if size == "S":
    bill += 35
  else:
    bill += 50
if extra_cheese == "Y":
  bill += 20
print(f"Your final bill is: ₹{bill}.")
```