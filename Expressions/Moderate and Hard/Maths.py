# Print sum, difference and product of 2 numbers

a = input("Please input a numerical value for a: ")
b = input("Please input a numerical value for b: ")


### Print the sum of a and b 
print("The sum of the two numbers is:", int(a)+int(b))

### Print the difference of a and b 
print("The difference between the two numbers is:", int(a)-int(b))

### Print the product of a and b
print("The product of the two numbers is:", int(a)*int(b))

### Print the quotient
print("The quotient is:", int(a)/int(b))



# Print a string and its length
abc = input("Please input a String value: ")
print("The string that you provided is", abc , "and it has a length of", len(abc))

# Print a floating point number and integer
xyz = float(input("Please input a floating point number: "))
ijk = int(xyz)

print("The floating point number is" , xyz, " and its integer value is", ijk) 


# Print the Name, Age and Grade of a person

rst = input("What is your name?: ")
yrsold = input("What is your age?: ")
score = input("What is your grade?: ")

print("Name:", rst)
print("Age:", yrsold)
print("Grade:", score)


# Perform mathematical operations on 2 numbers

h = float(input("Please provide a numerical value for h: " ))
k = float(input("Please provide a numerical value for k: " ))
operator = input("What do you want to do with h and k? (please type one of these values: (+ , - , * , /): ")

if operator == "+":
 print("The sum of h and k is", h+k)
elif operator == "-":
 print("The difference of the two numbers is", h-k)
elif operator == "*":
 print("The product of the two numbers is", h*k)
elif operator == "/":
 print("The division of the two numbers gives", h/k)
else:
 print("You have provided an incorrect mathematical operator, please provide the correct mathematical operators: (+ , - , * , /)")


# Check for the type of input (integer/float/string)

kln = input("Please type a value: " )

if int(kln) is type(5):
 print("The value you provided is of type, integer.")
elif float(kln) is type(7.0):
 print("The value you provided is of a floating type value.")
elif type(kln) is type("String"):
 print("The value you provided is a String")

# Find the type of variable when it is assigned different values

f = 5
print(f, "is of type,", type(f))
f = 7.0
print(f, "is of type,", type(f))
f = "String"
print(f, "is of type,", type(f))

f = 3.0
print(f, "is of type,", type(f))
f = "Python"
print(f, "is of type,", type(f))
f = 1
print(f, "is of type,", type(f))

f = "Maths"
print(f, "is of type,", type(f))
f = 10
print(f, "is of type,", type(f))
f = 8.0
print(f, "is of type,", type(f))

# Obtain the value in dollars and convert it to rupees

Dollars = input("Please provide the amount of money in INR: ")
print(float(Dollars)/82)
