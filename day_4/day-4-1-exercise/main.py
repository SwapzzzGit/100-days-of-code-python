import random
test_speed = int(input("Create a seed number:"))
random.seed(test_speed)
random_side = random.randint(0,1)
if random_side == 0:
  print("Heads")
else:
  print("Tails")