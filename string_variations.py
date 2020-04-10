#!/usr/bin/env python3.7

string_message = input("Enter a message ..")

print("Message in lowercase", string_message.lower())
print("Message in uppercase", string_message.upper())
print("Capitalised", string_message.capitalize())
print("Title Case ", string_message.title())
print("Words ..",string_message.split())
sorted_words = sorted(string_message.split())
print(sorted_words)
print(" first word .. ",sorted_words[0])
print("last word ....", sorted_words[-1])


