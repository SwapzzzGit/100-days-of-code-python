## Who's Paying the bill

# Problem Statement

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

# Problem Input

```
rushi, swapnil, aakarsh, nupur, wadala
```
# Problem Output

```
nupur is going to buy the meal today!
```
# Solution
```
import random
names_string = input("Give everyone's name saperated by comma\n")
names = names_string.split(",")
list_no = len(names)
random_choice = random.randint(0,list_no - 1)
print(f"{names[random_choice]}, will pay the bill.")
```