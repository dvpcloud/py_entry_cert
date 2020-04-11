#!/usr/bin/env python3.7

upper_number = int(input("Enter the upper range limit (integer) ..."))

for num in range(1,upper_number+1):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Buzz")
    elif num % 5 == 0:
        print(num)
    else:
        print(num)
