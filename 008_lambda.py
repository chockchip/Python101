from functools import reduce

""" 
Lampda function

syntax -> lambda arguments : expression

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Benefit:
The power of lambda is better shown when you use them as an anonymous function inside another function.
"""

def my_func(n):
    return lambda a: a**n

double = my_func(2)     # Create function for power 2
print(double(3))        


""" 
Map

Iterate like a complehensive but use the function instread
Can return value to be list

speed fater than loop
"""
items = [1, 2, 3, 4, 5]

# Map is faster that loop
square_items = list(map((lambda x: x ** 2),items))

print("*" * 30)
print(square_items)

""" 
Reduce

Iterate like a Map but return only single value
"""

# function for find max
f = lambda x, y: x if (x > y) else y

items_2 = [5, 102, 7, -4]

max_item = reduce(f, items_2)
print(max_item)

""" 
Filter

Iterate and return item that have bool to be True
"""

items_3 = [-2, -1, 0, 1, 2]
g = lambda x: x < 0

# => If use map it will return bool (x < 0)
# => If use filter it will return item that has bool True

filter_item = list(filter(g, items_3))
print(filter_item)