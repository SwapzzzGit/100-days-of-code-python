## Data Types

# Problem Statement

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


# Example Input

```
39
```

# Example Output

3 + 9 = 12

```
12
```

# Problem Output
```
two_digit_number = input("Type a two digit number: ")
d1 = int(two_digit_number[0])
d2 = int(two_digit_number[1])
d3 = d1 + d2
print(type(d1)) #checking type of varibles for self.
print(type(d2)) #checking type of varibles for self.
print(type(d3)) #checking type of varibles for self.
print(str(d1) + '+' + str(d2) + '=' + str(d3))
```
![2](2.gif)