# Enter a String and print its length

abc = input("Please enter a String: ")

print("The length of String, abc is", len(abc))


# Print the characters in a string one by one, in separate lines

xyz = input("Please enter a String: ")

print("\n")

print("The characters of above String is displayed one by one as below,\n")

for a in xyz:
  print(a)

# Find three characters, last three characters and reverse a string

xyz = input("Please enter a String: ")

print("\nThe first three characters of above string is,", xyz[:3])

print("\nThe last three characters of above string is,", xyz[(len(xyz)-3):])

# Reverse the string

ch =""

for i in xyz:
  ch = i + ch

print("\nThe reversal of above string is,", ch)


# Check if Python is present in the String provided by user

ijk = input("Please enter a String: ")

if "Python" in ijk:
    print("\nPython is present in the string.")
else:
  print("\nPython is not present in the string.")

# Print the uppercase of a string, which is provided as a user input

ijk = input("Please enter a String: ")

lmn = ijk.upper()

print("Uppercase of", ijk, "is", lmn)


### Moderate

# Print the number of vowels in a string provided by user

vowels = ['a','e','i','o','u']

asd = input("Please provide a string to count the number of vowels present in the string: ")

count = 0
plm = list(asd)

for j in plm:
  if j in vowels:
    count = count + 1
print("\nThere are", count, "vowels in the string provided.")


# Find out which string is lexicographically bigger, smaller or equal, out of two strings provided by user

AMD = input("Please provide a string: ")

NIVIDIA = input("Please provide another string: ")

if AMD == NIVIDIA:
  print("\nThe two strings provided are the same")
elif AMD > NIVIDIA:
  print("\nThe string,", AMD, "lexicographically  greater than", NIVIDIA)
elif AMD < NIVIDIA:
  print("\nThe string,", NIVIDIA, "lexicographically  greater than", AMD)

# Print the username from a user provided email address

email_addr = input("Please provide an email address: ")

email_list = email_addr.split('@')

print(email_list[0])

# Print the Name and Age of a person using % format operator

name = input("Please provide your Name: ")

age = input("\nPlease provide your Age: ")

print("\nHello %s, you are %s years old." % (name, age))


# Replace a character in a string with another character

wer = input("Please provide a String: ")

print(wer.replace('a','z'))

# Check if a string is a palindrome

ojb = input("Please provide a String: ")

rev_ojb=""

for ch in ojb:
  rev_ojb = ch + rev_ojb

if ojb == rev_ojb:
  print("The string,", ojb, "is a palindrome.")
else:
  print("The string,", ojb, "is not a palindrome.")

# Find a pattern in a String provided by user

jkl= input("Please provide a String: ")
tyu = jkl.split(" ")
#print(tyu)
count = 0

for k in tyu:
  if "is" in k:
    count = count + 1
print("The substring 'is' appeared", count, "times in the string provided,",jkl)

# Print the name, age and country of a person provided as user input

age = input("Please provide your age: ")

country = input("Please provide your country: ")

print("Name: %s %s" %(first_name, last_name))

print("Age: %s" % (age))

print("Country: %s" %(country))

# Print full name

name = input("Enter your name: ")
print("Hello " + name[:])
