# Variables
# Instructions

Write a program that switches the values stored in the variables a and b. 

# Input

```
a: 3
```

```
b: 5
```

# Expected Output

```
a: 5
```

```
b: 3
```

# Solution
```
a = input("a : ")
b = input("b : ")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)
```
![1](1.4%20variables.gif)