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