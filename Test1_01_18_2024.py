# Practice and Learning from LearnPython Basics. Author: Shaqib

#Interger
myint=7
print(myint)

#Floating Point Number
myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

#String
mystring = 'hello'
print(mystring)
#Double quotes can include apostrophes in a string of text.
mystring = "hello you're looking well"
print(mystring)

#Simple operators can be executed on numbers and strings
one = 1
two = 2
three = 3
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#Multiple variable assignments
a, b = 3,4
print(a,b)

#Mixing operators between numbers/strings is not supported
one = 1
two = 2
hello = "hello"

print("print(one + two + hello) will not work as there is a mix of string and number.")

#Variable exercise
#Change this code
mystring = hello
myfloat = 10.0
myint = 20
#Test code
if mystring == "hello":
    print("String : %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


#Lists
#Similar to arrays. Can contain any variable type, and unlimited amounts of them. 
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #prints 1
print(mylist[1]) #prints 2
print(mylist[2]) #prints 3

#Prints out 1,2,3
for x in mylist:
    print(x)

#Exception error for accessing an index that does not exist
mylist = [1,2,3]
print("print(mylist[10]) - This does not work as the index does not exist.")

#List Exercise
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings = []
strings.append("Hello")
strings.append("World")

names = ["John", "Eric", "Jessica"]

#Write code
second_name = names[1]
#Code will write out filled arrays and second name in the list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#Operators

number= 1 + 2 * 3 / 4.0
print(number)

remainder= 11 % 3
print(remainder)

#Two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Operators with strings
helloworld = "hello" + " " + "world"
print(helloworld)

#Multiple strings used to form a strong with a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Operators and lists together
even_numbers = [2,3,6,8]
odd_numbers = [1,3,5,7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

#New lists with repeating sequence with multiplication operator
print([1,2,3] * 3)

#Exercise
x = object()
y = object()

#Change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

#Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#String formatting
    
#Statement prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#Prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#String and non-string format
mylist = [1,2,3]
print("A list: %s" % mylist)

#Basic argument specifiers:

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

#Basic string operations
astring = "Hello world!"
astring2 = 'Hello world!'

print("Single quotes are ' '")

print(len(astring))         #len command prints out the character size of a string

print(astring.index("o"))   #4 is printed as the first occurence of o is 4 after the first character. First letter counts as 0.

print(astring.count("l"))   #This prints 3 as is counts the number of I's in the string

print(astring[3:7])         #Prints the letters in the string between slot 3 and 7.

print(astring[3:7])
print(astring[3:7:1])       #Known as extended slice syntax. Prints characters from 3 to 7, and skip one character. This form is as follows: [start:stop:step].

print(astring[::-1])        #Reverses the string.

print(astring.upper())      #Uppercase the entire string.
print(astring.lower())      #Lowercase the entire string.

print(astring.startswith("Hello"))          #True statement when compared to the string.
print(astring.endswith("asdfasfasdf"))      #False statement when compared to the string.

afewwords = astring.split(" ")              #Splits the string into a bunch of strings grouped together in a list.

#Exercise
s = "Strings are awesome!"
#Length needs to be 20
print("Length of s= %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) #Start to 5
print("The next five characters are '%s'" % s[5:10]) #Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last give characters are '%s'" % s[-5:]) #5th-form-last to end

# Convert everything to uppercase
print("Strings in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("Strings in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("Strings starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

#Conditions
x = 2
print(x == 2) #prints out True
print(x == 3) #prints False
print(x < 3) #prints True

#Boolean Condition
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# In operator condition
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#Python indentation defines code blocks, which is 4 spaces. Tabs and other space sizes work with consistent spacing.
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# Indentation example
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# 'is' operator condition
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False. Is matches the instances, not the values.

# Not operator condition
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# Exercise
# Change this code and make every statement true.
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# Loops
primes = [2,3,5,7]
for prime in primes:
    print(prime)

# Prints the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3,6):
    print(x)

# Prints out 3,5,7
for x in range(3,8,2):
    print(x)
# Range returns new list numbers of specified range. Xrange returns an iterator for efficiency.
    # Python 3 uses the range function, acting like xrange. Range function is zero based.

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1 # Same as count = count + 1

# Break and Continue statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break   # Break is ued to exit a loop or a while loop.

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue    # Continue is used to skip the current block, and return to the "for" or "while" statement.
    print(x)

# Else clause for loops?
# When loop condition of "for" or "while" statements fails then code part in "else" executes.
# If break statement goes inside the for loop then the "else" part is skipped.
# Else is executed even if there is a continue statement.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this can't print as the loop terminates because of the break but not from condition failure")

# Exercise
# Loop through and print all even numbers from the list in the same order they were received.
# Don't print any more numbers after 237 in the sequence.
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# Your code here
for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue

    print(number)

# Functions

# Block format example
# block_head:
   # 1st block line 
   # 2nd block line 
   # ...

# Functions defined using block word 'def', followed with function's name as block name.
def my_function():
    print("Hello From My Function!")

# Function receiving arguments (variable passed from the caller to the function).
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%
(username, greeting))
    
# Function returning value to the caller, keyword used: return.
def sum_two_numbers(a,b):
    return a + b

# Calling a function(s).
# Write function's name followed by (). Place arguments in brackets. Calling function written above.
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%
          (username, greeting))
    
def sum_two_numbers(a,b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you are great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

# Exercise
# Use an existing function, and add my own to create full functioning program.
# Add function named list_benefits() to return list of strings:
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together".
# Add function named build_sentence(info) which receives a single argument containing a string and
# return a sentence starting with the given string and ending with the string " is a benefit of functions!"

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "more readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - "is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# Classes and Objects
# Objects are a group of variables and functions into a single entity.
# Objects get their variables and functions from classes, which are basically templates to create objects.

# A basic class - 
class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class.")

# Objects are a collection of variables and functions in one entity. They get variables and functions from classes. Classes are a template to create objects.
    class MyClass:
        variable = "blah"

        def function(self):
            print("This is a message inside the class.")

# Assigning the above class(template) to an object does the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
# Variable "myobjectx" holds object of the class, 'MyClass', that has variable and function defined within the class classed 'MyClass'.

# Access object variable
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable

# This outputs the string "blah":
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)

# Multiple different objects of the same class. Each object contains independent copies of the variables in the class.
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "Yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# Accessing Object Functions
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
# Prints out the message above.

# init()
# This function is called when a class is being started. Assigns values in a class.
class NumberHolder:

    def _init_(self, number):
        self.number = number

# Exercise
# Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with name Fer.
# car2 is a blue van named Jump worth $10,000.00

# define the Vehicle class.
class Vehicle:
    name = ""
    kind = "Car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name,
    self.color, self.kind, self.value)
        return desc_str
    
# My code here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# Test code
print(car1.description())
print(car2.description())

# Dictionaries
# Similar to arrays, but work with keys and values instead of indexes. 
# Values are accessible with keys, which can be a string, number, list, etc. 

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Dictionary initialized with same values in this notation:
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# Iterating over dictionaries. Though it does not keep the order of values stored within.
# To iterate over key value pairs, use this syntax:
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Remove a value
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
# or remove a value this way
phonebook = {
    "John" : 938477566,
    "Jack" : 938377566,
    "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

# Exercise
# Add Jake to the phonebook with his number, and remove Jill.

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# My code here:
phonebook["Jake"] = 938273443
phonebook.pop("Jill")
print(phonebook)

# Testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# Modules and Packages
# Learning Material in separate file.

# Exercise
# Print an alphabetically sorted list of all functions in re module containing the word find:

import re

# My code here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))