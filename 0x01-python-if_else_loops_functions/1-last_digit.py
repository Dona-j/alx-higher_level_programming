#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str1 = f'Last digit of {number}'
str2 = f'is {last_digit}'
str1 = str1 + str2
if last_digit > 5:
	print(f'{str1} and is greater than 5')
elif last_digit == 0
	print(f'{str1} and is 0')
else:
	print(f'{str1} and is less than 6 and not 0')