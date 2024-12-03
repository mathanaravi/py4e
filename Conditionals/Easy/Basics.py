# Check if number is positive, negative or zero

z = int(input("Enter a number: "))

if z == 0:
 print(z, "has a value of zero")
elif z > 0:
 print(z, "is a positive number")
elif z < 0:
 print(z, "is a negative number")

# Check if one number is greater than the other or they are equal

a = int(input("Enter a numerical value for a: " ))
b = int(input("Enter a numerical value for b: " ))

if a == b:
 print(a, "is equals to", b)
elif a > b:
 print(a, "is more than", b)
elif a < b:
 print(b, "is more than", a)


# Check if a number entered is an integer

num = int(input("Please enter a number: "))

try:
  if type(num) is int:
    print(num, "is an integer.")
except:
  print("You have not entered a number")

