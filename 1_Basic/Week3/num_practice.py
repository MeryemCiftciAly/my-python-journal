# This a challenge for my intro to using number funcions

import random

print(" Challenge write a random number between 1 and 100 then check if the number is even")

some_num = random.randint(1,100)
print(some_num)
print(some_num % 2)

print("Random number:", some_num)

print("Is this number even or odd: Remainder when divided by 2?", some_num % 2)



import math
import random
from math import trunc

inputs = ['450','299.99','315.50','error', '89','-100']

clean_num = []

for items in inputs:
    try:
        number = abs(float(items))
        clean_num.append(number)
    except ValueError:
             print(f'The value error is: {items} ')

print("Cleaned numbers:", clean_num)

print("=" * 30)
print(f"This is rounding numbers")

print('=' * 30)
print(f"Rounding the results /n")
print()

values = [132.789, 1045.0, 59.955, 999.999]

for items in values:
      rnd_num = round(items, 2) #rounding to two decimal places
      print("Rounded:", rnd_num)
      print("Ceiling:", math.ceil(rnd_num)) #Rounding up
      print("Floor:", math.floor(rnd_num)) #Rounding down
      print()

