import random
names_string = input("Give everyone's name saperated by comma\n")
names = names_string.split(",")
list_no = len(names)
random_choice = random.randint(0,list_no - 1)
print(f"{names[random_choice]}, will pay the bill.")