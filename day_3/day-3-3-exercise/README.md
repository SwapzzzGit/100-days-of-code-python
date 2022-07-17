## BMI Calculator 2.0

# Problem Input

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# Example Input

```
weight = 85
```

```
height = 1.75
```

# Example Output

85 ÷ (1.75 x 1.75) =  27.755102040816325

```
Your BMI is 28, you are slightly overweight.
```

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```
# First Solution
```
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = int(weight/height ** 2)
if BMI < 18.511:
  print("Your BMI is " + str(BMI) + ", you are underweight.")
elif BMI >= 18.511 and BMI < 25:
    print("Your BMI is " +str(BMI) + ", you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print("Your BMI is " +str(BMI) + ", you are slightly overweight.")
elif BMI >= 30 and BMI < 35 :
  print("Your BMI is " +str(BMI) + ", you are obese.")
else :
  print("Your BMI is " +str(BMI) + ",you are clinically obese.")
```
# Second Solution
```
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight/height ** 2)
print(BMI)
if BMI < 18.511:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.511 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35 :
  print(f"Your BMI is {BMI}, you are obese.")
else :
  print(f"Your BMI is {BMI},you are clinically obese.")
```
