import math
import random
from math import trunc

expenses = ['199.50', '205.25', 'error', '-45', '320.99']

cleaned_values = [] # creating an empty variable to hold the clean expense values

for items in expenses: #Cleaning each  value: convert to float, use abs()
    try:
        clean_exp = abs(float(items)) # converting values
        cleaned_values.append(clean_exp)
    except ValueError:
        print(f'Invalid expense value is: {items}')

print(f'\nClean Expenses are: {cleaned_values}')

print("=" * 30)
print("Rounding Results: \n")

for values in cleaned_values:
        rounded_value = round(values, 2)
        print(f'Original Value: {values}')
        print(f'Rounded Value: {rounded_value}')
        print(f'Celinng: {math.ceil(rounded_value)}')
        print(f'Flooring: {math.floor(rounded_value)}')
        print()



