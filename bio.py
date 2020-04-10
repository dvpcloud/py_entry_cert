name = input ("what is your name ? ")
colour = input("what is your favourite colour ?")
age = int(input("what is your age ? "))

print(f"{name} is {age} years old and favourite colout is {colour}")

#other way of printing things
print(name,end=" ")
print("is "+ str(age) + " years old", end = " ")
print("and likes colour " + colour + ".", end = " ")

#other way of printing things
print(name,"is ",str(age)," years old", " and likes colour " , colour + ".", sep = " - ")

