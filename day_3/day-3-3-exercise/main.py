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