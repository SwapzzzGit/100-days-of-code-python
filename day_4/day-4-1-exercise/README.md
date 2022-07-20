## Heads or Tails

# Problem Statement

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

# Example Output

```
Heads
```

or

```
Tails
```


# Solution
```
import random
test_speed = int(input("Create a seed number:"))
random.seed(test_speed)
random_side = random.randint(0,1)
if random_side == 0:
  print("Heads")
else:
  print("Tails")
```