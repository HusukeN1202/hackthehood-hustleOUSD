# Debugging Activity - Husuke Nishioka

# Code snippet 1

x = 10
y = 2
result = x / y
print("Result:", result)
# It was a ZeroDivisionError, so I changed the value of the divisor (y) to something else.

# Code snippet 2

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

# Off by 1 error ^

# Code snippet 3
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area

#  The colon after the function  was missing. (Syntax error)

# Code snippet 4

def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# Another syntax error, it was missing the colon after the if and else statement. ^

# Code snippet 5

for i in range(5):
   print(i)

#The same as earlier.

# Code snippet 6

def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))
# It was missing the  + between "Hello, " and name

# Code snippet 7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

# Indentation  error

#  Code  snippet 8

def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))  #No  errors

#Code snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": # "bob" was a  true value
   print("Hello, " + name)
else:
   print("Hello, stranger!")

#Code snippet 10
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))
# Zero division error