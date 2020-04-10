#!/usr/bin/env python3.7

print("String methods")

valid_string = input("enter a message ..:")
print("First character = ",valid_string[0])
print("Last character = ", valid_string[-1])
mid = int(len(valid_string)/2)
print("Middle character = ",valid_string[mid])
print(" Event index characters ", valid_string[::2])
print("Odd index characters ",valid_string[1::2])
print("reverse characters ", valid_string[::-1])
