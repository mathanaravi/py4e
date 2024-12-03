# Check the eligibility to vote

age = int(input("Enter your age: "))

if age >= 18:
  print("You are eligible to vote.")
else:
 print("You are not eligible to vote.")

# Check the value of a number input by user

number = int(input("Please enter a number: "))
if number > 0:
  if (number%2) == 0:
    print(number, "is an even number")
  else:
    print(number, "is an odd number")
elif number < 0:
  print(number, "is negative")
else:
  print("Number is zero")

# Compare the lengths of 2 different strings

abc = input("Please provide the first string: ")
fgh = input("Please provide the second string: ")

if len(abc) > len(fgh):
  print("The string,", abc, "is larger than the string,", fgh)
elif len(abc) < len(fgh):
  print("The string,",fgh, "is larger than the string,", abc)
else:
  print("Both strings,", abc, "and", fgh, "are equal in length")

# Divide two numbers

a = int(input("Please input a number: "))
b = int(input("Please input another number: "))

try:
  print(a/b)
except ZeroDivisionError:
  print("Second number provided is zero.", "We will not have an numerical output when dividing", a, "by", b, ".")

# Obtain the grade from a student's marks

marks=int(input("What is your mark?: "))

if marks >= 90:
  print("Your grade is A")
elif (marks >=75 and marks <90):
  print("Your Grade is B")
elif (marks >=50 and marks <75):
  print("Your Grade is C")
elif marks <50 and marks>=0:
  print("You have failed")
else:
  print("Print enter your marks correctly")

# Check the suitability of password being set

passwd = input("Please enter a password: ")

if len(passwd)<=7:
  print("Your password is too short")
if (passwd.isupper() is True) or (passwd.islower() is True) :
  print("You need to include both uppercase and lowercase letters in the password")
if passwd.isnumeric() is False:
  print("You need to include at least a number in your password")


# try and except block with mathematical operation on 2 blocks

h = float(input("Please provide a numerical value for h: " ))
k = float(input("Please provide a numerical value for k: " ))
operator = input("What do you want to do with h and k? (please type one of these values: (+ , - , * , /): ")

try:
 if operator == "+":
   print("The sum of h and k is", h+k)
 elif operator == "-":
   print("The difference of the two numbers is", h-k)
 elif operator == "*":
   print("The product of the two numbers is", h*k)
 elif operator == "/":
   print("The division of the two numbers gives", h/k)
except ZeroDivisionError:
   operator != "+" or operator != "-" or operator != "*" or operator != "/"
   print("Please provide correct mathematical operator")
   break
   print("You cannot divide by zero")
