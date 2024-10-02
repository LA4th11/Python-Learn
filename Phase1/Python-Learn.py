#FIRST OUTPUT FOR PYTHON
print("Hello Master")
#PYTHON IDENTATION
if 5 > 2:
  print("5 > 2 = YES")
#THIS IS THE EXAMPLE OF COMMENTS  <---
#PYTHON VARIABLES
a = 5
b = 5.0
c = "Hello"
print(type(a), a)
print(type(b), b)
print(type(c), c)
#CAMEL CASE
myVariable = "hello Hotdog"
#PASCAL CASE
MyVariable = "Hello Hotdog"
#SNAKE CASE
my_variable = "hello_hotdog"
#MANY VALUES TO MULTIPLE VARIABLES
x,y,z = "apple", "orange", "banana"
print(x)
print(y)
print(z)
#ONE VALUE TO MULTIPLE VARIABLES
x=y=z = "grape"
print(x)
print(y)
print(z)
#UNPACK A COLLECTION
fruits = ["melon", "guava", "strawberry"]
x,y,z = fruits
print(x)
print(y)
print(z)
#PYTHON OUTPUT VARIABLES - COMMA
x = "CHICK"
y = "BOY"
print(x, y)#OUTPUT -> CHICK BOY
#PYTHON OUTPUT VARIABLES - PLUS OPERATION
x = "CHICK"
y = "BOY"
print(x + y)#OUPUT -> CHICKBOY
#PYTHON OUTPUT - FSTRING
wife = "Micaella Laforteza"
print(F"My wife's name is {wife}")
#GLOBAL VARIABLES
x = "beautiful"

def myWife(): #DECLARING FUNCTION
  print(F"Micaella is so {x}.")
  
myWife()
#GLOBAL KEYWORD
def globalVariable():
  global x #<-- USING GLOBAL KEYWORD TO USE AS A GLOBAL VARIABLE INSIDE THE FUNCTION
  x = "cute"

globalVariable()
print(F"Micaella is so {x}.")
#DATA TYPES
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType
#MULTILINE STRINGS
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#SLICE TO THE END
b = "Hello Master"
print(b[0:]) #[start 0 index : find 1st index]
print(b[1:])
print(b[2:])
#UPPER CASE
a = "Hello Master"
print(a.upper())
#LOWER CASE
print(a.lower())
#REPLACE STRING
replace = a.replace("Hello", "Bye")
print(replace)
# -->ESCAPE CHARACTERS <--
# \'   Single Quote
# \\   Backslash
# \n   New Line
# \r   Carriage Return
# \t   Tab
# \b   Backspace
# -->PYTHON ARITHMETIC OPERATORS<--
# +   Addition         -> x + y    Adds two values
# -   Subtraction      -> x - y    Subtracts second value from first
# *   Multiplication   -> x * y    Multiplies two values
# /   Division         -> x / y    Divides first value by second
# %   Modulus          -> x % y    Returns the remainder of the division
# **  Exponentiation   -> x ** y   Raises first value to the power of the second
# //  Floor division   -> x // y   Divides and returns the largest integer less than or equal to the result
# -->PYTHON ASSIGNMENT OPERATORS<--
# =    Assignment          -> x = 5        Assigns 5 to x
# +=   Addition assignment  -> x += 3      Equivalent to x = x + 3
# -=   Subtraction assignment-> x -= 3      Equivalent to x = x - 3
# *=   Multiplication assignment -> x *= 3   Equivalent to x = x * 3
# /=   Division assignment   -> x /= 3      Equivalent to x = x / 3
# %=   Modulus assignment    -> x %= 3      Equivalent to x = x % 3
# //=  Floor division assignment -> x //= 3  Equivalent to x = x // 3
# **=  Exponentiation assignment -> x **= 3  Equivalent to x = x ** 3
# &=   Bitwise AND assignment -> x &= 3      Equivalent to x = x & 3
# |=   Bitwise OR assignment  -> x |= 3      Equivalent to x = x | 3
# ^=   Bitwise XOR assignment -> x ^= 3      Equivalent to x = x ^ 3
# >>=  Bitwise right shift assignment -> x >>= 3 Equivalent to x = x >> 3
# <<=  Bitwise left shift assignment -> x <<= 3 Equivalent to x = x << 3
# :=   Walrus operator       -> x := 3      Assigns 3 to x and returns
# -->PYTHON COMPARISON OPERATORS<--
# ==  Equal                     -> x == y    Checks if x is equal to y
# !=  Not equal                 -> x != y    Checks if x is not equal to y
# >   Greater than              -> x > y     Checks if x is greater than y
# <   Less than                 -> x < y     Checks if x is less than y
# >=  Greater than or equal to   -> x >= y    Checks if x is greater than or equal to y
# <=  Less than or equal to      -> x <= y    Checks if x is less than or equal to y
# -->PYTHON LOGICAL OPERATORS<--
# and  Returns True if both statements are true    -> x < 5 and x < 10
# or   Returns True if one of the statements is true -> x < 5 or x < 4
# not  Reverse the result, returns False if the result is true -> not x < 5
#PYTHON LISTS
car = ["BMW", "HONDA", "TOYOTA"]
number = [1, 2, 5, 4]
ask = [True, False]
thisList = list(("apple", "banana", "grapes"))
print(car)
print(number)
print(ask)
print(thisList)
#PYTHON-ACCESS LIST ITEMS
print(car[1])#OUTPUT -> HONDA
#NEGATIVE INDEXING
print(car[-1])#OUTPUT -> TOYOTA
#CHECK IF ITEM EXISTS
if "BMW" in car:
  print(F"Yes, {car[0]} is here.")
#PYTHON-CHANGE LIST ITEMS
car[0] = "FERRARI"
print(car)
#CHANGE A RANGE OF ITEM VALUES
car[0:2] = ["BUGATTI", "BENTLEY"]
print(car)
#INSERT ITEMS
car.insert(1, "CHERRY")
print(car)
#PYTHON-ADD LIST ITEMS
car.append("BUGATTI") #IT'S INSERT IN THE LAST OF THE ARRAY.
print(car)#OUTPUT -> ['BUGATTI', 'CHERRY', 'BENTLEY', 'TOYOTA', 'BUGATTI']
#EXTEND LIST
fruits = ["MANGO", "PINEAPPLE", "PAPAYA"]
car.extend(fruits)
print(car)
#PYTHON-REMOVE LIST ITEMS
car.remove("MANGO")
print(car)
#REMOVE THE SPECIFIED INDEX
car.pop(1)
print(car)
#DEL KEYWORD
del car[0] #OR CAN DELETE INTIRE ARRAY EXAMPLE: del car
print(car)
#CLEAR THE LIST
car.clear() #CLEAR INTIRE LIST OF ARRAY BUT THE BRACKET ARE THEIR
print(car)
#PYTHON-LOOP LISTS
