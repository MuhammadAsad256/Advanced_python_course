# Exercise 1: Basic Lambda Functions
# Question: Create a lambda function that multiplies two numbers and returns the result. Use this lambda function to multiply 5 by 7.

multiply = lambda x, y: x * y
result = multiply(5, 7)
print(result)

# Exercise 2: Using map with Lambda Functions
# Question: You have a list of numbers [1, 2, 3, 4, 5]. Use the map function and a lambda function to create a new list where each number is increased by 10.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_numbers = list(map(lambda x: x + 10, numbers))
print(sum_numbers)

# Exercise 3: Combining filter and reduce with Lambda Functions
# Question: Given a list of numbers [3, 6, 9, 12, 15, 18, 21], use the filter function to select numbers greater than 10. Then, use the reduce function to calculate the sum of the filtered numbers.

from functools import reduce
numbers = [3, 6, 9, 12, 15, 18, 21]

filtered_numbers = list(filter(lambda x :x>10 , numbers))

sum_filtered = reduce(lambda x, y: x + y, filtered_numbers)
print(sum_filtered)