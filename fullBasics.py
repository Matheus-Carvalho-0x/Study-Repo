# Python can be treated in a procedural way, an object-oriented way or a functional way.

# Check the Python version of the editor:
# import sys
# print(sys.version)

# You can write multiple statements on one line by separating them with ;
# print("Hello"); print("How are you?"); print("Bye bye!")

# If you want to print multiple words on the same line, you can use the end parameter:
print("Hello World!", end=" ")
print("I will print on the same line.")

# You can combine text and numbers in one output by separating them with a comma:
print("I am", 35, "years old.")

# Multiline Comments
"""
This is a comment
written in
more than just one line
"""

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Camel Case: myVariableName = "John"
# Pascal Case: MyVariableName = "John"
# Snake Case: my_variable_name = "John"

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Note: Make sure the number of variables matches the number of values, or else you will get an error.
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into
#  variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# You can also use the + operator to output multiple variables:
print(x + y + z)  # If there isn't space it will print Pythonisawesome

# If you create a variable with the same name inside a function, this variable will be local, and can only be
#  used inside the function. The global variable with the same name will remain as it was, global and with the
#  original value.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


# BUILT-IN DATA TYPES:
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

# Setting data types:
x = 1j	                    complex
x = range(6)	            range
x = b"Hello"	            bytes
x = bytearray(5)	        bytearray
x = memoryview(bytes(5))	memoryview
x = None	                NoneType

x = complex(1j)	            complex
x = range(6)	            range
x = bytes(5)	            bytes	
x = bytearray(5)	        bytearray	
x = memoryview(bytes(5))	memoryview
"""

# FLOAT:
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3        # 35*10³
y = 12E4        # 12*10⁴
z = -87.7e100   # -87.7*10¹⁰⁰

print(type(x))
print(type(y))
print(type(z))

# COMPLEX:
# Note: You cannot convert complex numbers into another number type.


# There may be times when you want to specify a type on to a variable. This can be done with casting.
# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.


# MULTILINE STRINGS:
# Note: in the result, the line breaks are inserted at the same position as in the code.
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# You can return a range of characters by using the slice syntax.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
# By leaving out the start index, the range will start at the first character.
# By leaving out the end index, the range will go to the end.
# Use negative indexes to start the slice from the end of the string.
# We can combine strings and numbers by using f-strings or the format() method!
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number
# with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

"""
# BELOW I HAD TO USE 1 ESCAPE CHAR EXTRA SO I COULD EVADE SYNTAX ERROR.
Escape Characters
Other escape characters used in Python:

Code	Result
\\'	Single Quote	
\\	Backslash	
\\n	New Line	
\\r	Carriage Return	    *
\\t	Tab	
\\b	Backspace	
\\f	Form Feed	        *
\\ooo	Octal value	    *
\\xhh	Hex value       *


# --- String Methods ---
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

# One more value, or object in this case, evaluates to False, and that is if you have an object
# that is made from a class with a __len__ function that returns 0 or False:


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# OPERATORS:
# Floor division always returns an integer.
# It rounds DOWN to the nearest integer.

# &=	x &= 3	x = x & 3       * Makes no f sense
# |=	x |= 3	x = x | 3       * Makes no f sense
# ^=	x ^= 3	x = x ^ 3       * Makes no f sense
# >>=	x >>= 3	x = x >> 3      * Makes no f sense
# <<=	x <<= 3	x = x << 3      * Makes no f sense
# :=	print(x := 3)	x = 3


# IDENTITY OPERATORS:
# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)


"""
Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2


EXAMPLE:
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(6 & 3)
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the & operator compares the bits and returns 0010, which is 2 in decimal.


The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(6 | 3)
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the | operator compares the bits and returns 0111, which is 7 in decimal.


The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(6 ^ 3)
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
"""


"""
Precedence Order
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
"""

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
# a = 5
# b = 2
# if a > b: print("a is greater than b")    # bad practice pep8 don't allow me
# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
a = 2
b = 330
print("A") if a > b else print("B")
# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""
# Example:
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

# WHILE LOOP:
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# FUNCTIONS:
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# --- From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
# The phrase Keyword Arguments is often shortened to kwargs in Python documentation.
# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
    print("Hello", name)


my_function("Emil")

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:


def my_function(*, name):
    print("Hello", name)


my_function(name="Emil")

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:


def my_function(a, b, /, *, c, d):
    return a + b + c + d


result = my_function(5, 10, c=15, d=20)
print(result)

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.
# The order must be:
# regular parameters
# *args
# **kwargs

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.


def my_function(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
result = my_function(*numbers)  # Same as: my_function(1, 2, 3)
print(result)

# Unpacking Dictionaries with **
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them:


def my_function(fname, lname):
    print("Hello", fname, lname)


person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)  # Same as: my_function(fname="Emil", lname="Refsnes")

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.


def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x


print(myfunc1())

# ====================================================================================================================================
# ----- DECORATORS -----
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.
# !!! Study more decorators.
# changecase is the decorator
# myinner is A wrapper (the decorator can have multiple levels of wrapper)
#  (is the one who gets the args if the decorated func has args)


def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())

# Arguments in the Decorated Function
# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:


def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))

# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level.
# Apparently all the new wrapper levels goes above the func arg


def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase


@changecase(1)
def myfunction():
    return "Hello Linus"


print(myfunction())

# Multiple Decorators
# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# !!!!!!!!Decorators are called in the reverse order, starting with the one closest to the function.


def changecase(func):
    def myinner():
        return func().upper()
    return myinner


def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner


@changecase
@addgreeting
def myfunction():
    return "Tobias"


print(myfunction())

# --- FUNCTIONS METADATA ---
# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.


def myfunction():
    return "Have a great day!"


print(myfunction.__name__)

# But, when a function is decorated, the metadata of the original function is lost.


def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)

# !!!!To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's
#  name and docstring.
"""
import functools

def changecase(func):
  @functools.wraps(func)        # You use this functools.wraps as a decorator to the innerfunction in the decorator
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
"""

# --- LAMBDA ---
# x = lambda a : a + 10
# print(x(5))
# !!!Interesting use:


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


# --- RECURSION ---
# Recursion Depth Limit
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
# import sys
# print(sys.getrecursionlimit())
# !!!!!!!If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


# --- GENERATORS ---
# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)

# Generators Saves Memory
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:


def large_sequence(n):
    for i in range(n):
        yield i


# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# Using next() with Generators
# You can manually iterate through a generator using the next() function:


def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"


gen = simple_gen()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

# When there are no more values to yield, the generator raises a StopIteration exception:


def simple_gen():
    yield 1
    yield 2


gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen))  # This will raise StopIteration

# Generator Expressions:
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

# Fibonacci Sequence Generator
# Interesting solution:


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
    print(next(gen))

# Generator Methods
# Generators have special methods for advanced control:
# send()    The send() method allows you to send a value to the generator:


def echo_generator():
    while True:
        received = yield
        print("Received:", received)


gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")

# close()   The close() method stops the generator:


def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")


gen = my_gen()
print(next(gen))
gen.close()


# -------- __iter__() --------
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# The for loop actually creates an iterator object and executes the next() method for each loop.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
