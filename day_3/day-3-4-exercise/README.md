## Leap Year

# 💪This is a Difficult Challenge 💪

# Problem Input

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
 
# Example Input 1

```
2400
```

# Example Output 1

```
Leap year.
```

# Example Input 2

```
1989
```

# Example Output 2

```
Not leap year.
```

# Solution

```
year = int(input("Which year do you want to check? "))
if year % 4 ==0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("LEAP YEAR")
    else:
      print("NOT A LEAP YEAR.")
  else:
    print("LEAP YEAR")
else:
  print("NOT LEAP YEAR")
  ```