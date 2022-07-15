## Your Life in Weeks

# Problem Input

Calculate Life in Weeks and realised just how little time we actually have. assume final age is 90.

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

It will take your current age as the input and output a message with our time left in this format:

> You have x days, y weeks, and z months left. 

Where x, y and z are replaced with the actual calculated numbers. 

# Example Input

```
56
```

# Example Output

```
You have 12410 days, 1768 weeks, and 408 months left.
```

# Problem Output
```
age = input("What is your current age?")
final_age = 90 - int(age)
days = 365 * final_age
week = 52 * final_age
months = 12 * final_age

print(f"You have {days} days, {week} weeks, and {months} months left.")
```