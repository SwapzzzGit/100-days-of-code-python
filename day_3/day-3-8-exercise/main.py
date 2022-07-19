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