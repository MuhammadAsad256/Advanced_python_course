#                               Programming Tasks for refreshing
# Q1:- Calculate the Area of a Rectangle:

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

# Q2:- Check if a Number is Even or Odd:

number = int(input("Enter a number: "))
if (number % 2) == 0 :
    print(f"your enter number {number} is even.")
else:
    print(f"your enter numer {number} is odd.")

# Q3:- Reverse a String:

user_input = input("Enter a string: ")
print(f"Reversed string: {user_input[::-1]}")

# Q4:- Find the Factorial of a Number:

num = int(input("Enter a Number: "))

factorial_num = 1

if num < 0 :
    print("The factorial of a number less than 0 does not exist")
if num > 0:
    for i in range (1,num+1):
        factorial_num = factorial_num * i
print(f"Factorial of {num} is: {factorial_num}")

# Q5:- Check if a String is Palindrome or Not:

def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter word... ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome")       
else:
    print(f"{input_string} is not a palindrome")

# Q6:- Generate Fibonacci Series up to n terms:



# Q7:- Find the Largest Among Three Numbers:

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)

# Q8:- Calculate Simple Interest:

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_period = float(input("Enter the time period in years: "))
simple_interest = (principal_amount * rate_of_interest * time_period) / 100
print("Simple Interest:", simple_interest)

# Q9:- Convert Celsius to Fahrenheit:

temperature = float(input("Enter temperature in Celsius: "))
result = (9/5) * temperature + 32
print(f"Temperature in Fahrenheit: {result}")

# Q10:- Check Leap Year:

year = int(input("Enter a year: "))

if (year % 400==0) and (year % 100==0):
    print(f"{year} is a leap year.")
if (year % 4==0) and (year % 100!=0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")


#                               Programming Challenges

# Q1:- Find the Median of Three Numbers:

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    median = num1
elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    median = num2
else:
    median = num3

print("Median is", median)

# Q2:- Count the Number of Words in a Sentence:

str = input("enter sentence: ")
s = 0
ch = 0
for i in str:
    if i == " ":
        if ch!=0:
            s=s+1
        ch = 0
    else:
        ch=ch+1
    
if ch!= 0:
    s=s+1
print(s) 

# Q3:- Calculate the Sum of Digits in a Number:

number = int(input("Enter a number: "))

sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)
    
print("Sum of digits:", sum_of_digits)

# Q4:- Find the Longest Common Prefix in a List of Strings:
# Q5:- Check if a Number is a Prime Number:

num = int(input("Enter a number: "))

if num > 1:
   # check condition
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not prime number")
           break
   else:
       print(num,"is prime number")