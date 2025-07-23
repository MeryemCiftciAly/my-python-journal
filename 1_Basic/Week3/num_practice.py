# This a challenge for my intro to using number funcions

import random

print(" Challenge write a random number between 1 and 100 then check if the number is even")

some_num = random.randint(1,100)
print(some_num)
print(some_num % 2)

print("Random number:", some_num)

print("Is this number even or odd: Remainder when divided by 2?", some_num % 2)