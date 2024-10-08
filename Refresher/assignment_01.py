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

first_num = 0 
second_num = 1
print(first_num)

for i in range (10):
    print(second_num)
    third_num = first_num + second_num
    first_num = second_num
    second_num = third_num

# Q7:- Find the Largest Among Three Numbers:

numbers = input("Enter three numbers separated by space: ").split()
num1, num2, num3 = map(int, numbers)

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The Largest Number is:", largest)

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

numbers = input("Enter three numbers separated by space: ").split()
num1, num2, num3 = map(int, numbers)

if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    median = num1
elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    median = num2
else:
    median = num3

print("The Median Number is:", median)

# Q2:- Count the Number of Words in a Sentence:

str = input("enter sentence: ")
words = str.split()
print(len(words))

# Q3:- Calculate the Sum of Digits in a Number:

number = int(input("Enter a number: "))

sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)
    
print("Sum of digits:", sum_of_digits)

# Q4:- Find the Longest Common Prefix in a List of Strings:

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strings = input("Enter strings separated by space: ").split()
print("Longest common prefix:", longest_common_prefix(strings))

# Q5:- Check if a Number is a Prime Number:

num = int(input("Enter a number: "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not prime number")
           break
   else:
       print(num,"is prime number")

#                        Bonus
# Q1:- Find the Longest Consecutive Sequence in a List of Integers:

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    long_sequence = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
    return long_sequence

nums = input("Enter integers separated by space: ").split()
nums = [int(num) for num in nums]
print("Longest consecutive sequence length:", longest_consecutive_sequence(nums))
