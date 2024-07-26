# Question: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.

# Input: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Expected Output: ['banana', 'cherry', 'elderberry']


fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
greater_fruits = list(filter(lambda x: len(x) > 5, fruits))
print(greater_fruits)


# Question: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.

# Input: [2, 4, 6, 8, 10]
# Expected Output: 122880 (Product of [4, 8, 12, 16, 20])

from functools import reduce

numbers = [2, 4, 6, 8, 10]

double_numbers = list(map(lambda x: x * 2, numbers))

result = reduce(lambda x, y: x * y, double_numbers)

print(result)  